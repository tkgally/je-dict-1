/**
 * Home-page search for je-dict-1.
 *
 * Data (search-index.js):
 *   SEARCH_INDEX.japanese / romaji / english / forms — key -> numeric id or [ids]
 *   SEARCH_ENTRIES[num] = [id, headword (furigana notation), reading, gloss, pos, tier b/c/g]
 *
 * Query handling:
 *   - Japanese text: exact headword/reading, then conjugated forms, then prefix,
 *     then substring matches. Katakana input is also tried as hiragana.
 *   - Latin text ("auto"): romaji and English are both searched and merged —
 *     romaji exact/prefix hits first, then English hits.
 *   - Romaji is normalized to the Hepburn used in the index: kunrei/nihon-shiki
 *     spellings (si, tu, hu, zi, ti, sya, tya, zya, jya...), macrons/circumflexes
 *     (ā ī ū ē ō → aa ii uu ee/ei ou/oo), "m" before b/p/m → n, and apostrophes,
 *     hyphens and spaces are dropped. Long vowels must otherwise be written out
 *     (toukyou); "nn" is left alone because it is ambiguous.
 *   - English: every query word must prefix-match an indexed gloss word of the
 *     entry (AND). Function words like "to" are ignored.
 *   Ranking: exact > form > prefix > substring; ties by tier (basic, core,
 *   general) then reading. Results are shown 50 at a time.
 */
(function() {
    'use strict';

    var PAGE_SIZE = 50;
    var TIER_NAMES = { b: 'basic', c: 'core', g: 'general' };
    var TIER_RANK = { b: 0, c: 1, g: 2 };
    // Keep in sync with ENGLISH_STOPWORDS in search_index_builder.py
    var STOPWORDS = { to: 1, a: 1, an: 1, the: 1, of: 1, or: 1, and: 1, 'in': 1, on: 1, be: 1, 'for': 1, 'with': 1, by: 1, at: 1 };

    // Rank buckets (lower is better)
    var RANK = { exact: 0, form: 1, prefix: 2, substring: 3, enPhrase: 4, enWord: 5, enPrefix: 6 };

    var searchInput = document.getElementById('search-input');
    var searchButton = document.getElementById('search-button');
    var resultsSection = document.getElementById('results-section');
    var resultsHeading = document.getElementById('results-heading');
    var resultsList = document.getElementById('results-list');
    var showMoreButton = document.getElementById('show-more-button');

    var current = { results: [], shown: 0 };
    var keyCache = {};

    function keysOf(table) {
        if (!keyCache[table]) keyCache[table] = Object.keys(window.SEARCH_INDEX[table] || {});
        return keyCache[table];
    }

    function idList(value) {
        return Array.isArray(value) ? value : [value];
    }

    function getEntry(num) {
        var row = window.SEARCH_ENTRIES && window.SEARCH_ENTRIES[num];
        if (!row) return null;
        return { num: num, id: row[0], headword: row[1], reading: row[2], gloss: row[3], pos: row[4], tier: row[5] };
    }

    function dirRange(id) {
        var n = Math.floor(parseInt(id.slice(0, 5), 10) / 500) * 500;
        return ('00000' + n).slice(-5);
    }

    // Headword text is HTML-escaped at build time; only furigana braces are converted here.
    function rubyHtml(text) {
        return text.replace(/\{([^|{}]+)\|([^}]+)\}/g, '<ruby>$1<rp>(</rp><rt>$2</rt><rp>)</rp></ruby>');
    }

    function plainHeadword(text) {
        return text.replace(/\{([^|{}]+)\|([^}]+)\}/g, '$1');
    }

    function hasJapanese(text) {
        return /[぀-ゟ゠-ヿ一-龯㐀-䶿]/.test(text);
    }

    function katakanaToHiragana(text) {
        return text.replace(/[ァ-ヶ]/g, function(ch) {
            return String.fromCharCode(ch.charCodeAt(0) - 0x60);
        });
    }

    // ── Romaji normalization ────────────────────────────────────────────
    function normalizeRomaji(query) {
        var q = query.toLowerCase().replace(/['’\-\s]+/g, '');
        q = q.replace(/[āâ]/g, 'aa').replace(/[īî]/g, 'ii').replace(/[ūû]/g, 'uu');
        // ē/ō are ambiguous (ei/ee, ou/oo): expand into all spellings below
        q = q.replace(/[ēê]/g, 'E').replace(/[ōô]/g, 'O');
        q = q.replace(/sh?y([auo])/g, 'sh$1');       // sya/shya -> sha
        q = q.replace(/[tc]h?y([auo])/g, 'ch$1');    // tya/chya -> cha
        q = q.replace(/[zj]y([auo])/g, 'j$1');       // zya/jya -> ja
        q = q.replace(/dy([auo])/g, 'j$1');          // dya -> ja
        q = q.replace(/si/g, 'shi').replace(/zi/g, 'ji').replace(/ti/g, 'chi')
             .replace(/tu/g, 'tsu').replace(/hu/g, 'fu').replace(/du/g, 'zu').replace(/dzu/g, 'zu');
        q = q.replace(/m([bpm])/g, 'n$1');
        // Expand E -> ee|ei and O -> ou|oo (at most 3 ambiguous vowels are expanded)
        var variants = [''];
        var ambiguous = 0;
        for (var i = 0; i < q.length; i++) {
            var ch = q[i];
            var options = null;
            if ((ch === 'E' || ch === 'O') && ambiguous < 3) {
                options = ch === 'E' ? ['ee', 'ei'] : ['ou', 'oo'];
                ambiguous++;
            } else if (ch === 'E') {
                options = ['ee'];
            } else if (ch === 'O') {
                options = ['ou'];
            }
            var next = [];
            for (var v = 0; v < variants.length; v++) {
                if (options) {
                    for (var o = 0; o < options.length; o++) next.push(variants[v] + options[o]);
                } else {
                    next.push(variants[v] + ch);
                }
            }
            variants = next;
        }
        return variants;
    }

    // ── Matching ────────────────────────────────────────────────────────
    // hits: num -> { rank, formOf }  (keeps the best rank per entry)
    function addHit(hits, num, rank, form) {
        var existing = hits[num];
        if (!existing || rank < existing.rank) {
            hits[num] = { rank: rank, form: form || (existing && existing.form) || '' };
        } else if (form && !existing.form) {
            existing.form = form;
        }
    }

    function searchJapanese(query, hits) {
        var index = window.SEARCH_INDEX;
        var variants = [query];
        var hira = katakanaToHiragana(query);
        if (hira !== query) variants.push(hira);

        variants.forEach(function(q) {
            if (index.japanese[q] !== undefined) {
                idList(index.japanese[q]).forEach(function(num) { addHit(hits, num, RANK.exact); });
            }
            if (index.forms && index.forms[q] !== undefined) {
                idList(index.forms[q]).forEach(function(num) { addHit(hits, num, RANK.form, q); });
            }
        });
        keysOf('japanese').forEach(function(key) {
            for (var i = 0; i < variants.length; i++) {
                var q = variants[i];
                if (key === q) continue;
                if (key.indexOf(q) === 0) {
                    idList(index.japanese[key]).forEach(function(num) { addHit(hits, num, RANK.prefix); });
                } else if (key.indexOf(q) !== -1) {
                    idList(index.japanese[key]).forEach(function(num) { addHit(hits, num, RANK.substring); });
                }
            }
        });
    }

    function searchRomaji(query, hits) {
        var index = window.SEARCH_INDEX;
        var variants = normalizeRomaji(query);
        variants.forEach(function(q) {
            if (index.romaji[q] !== undefined) {
                idList(index.romaji[q]).forEach(function(num) { addHit(hits, num, RANK.exact); });
            }
        });
        keysOf('romaji').forEach(function(key) {
            for (var i = 0; i < variants.length; i++) {
                var q = variants[i];
                if (key !== q && key.indexOf(q) === 0) {
                    idList(index.romaji[key]).forEach(function(num) { addHit(hits, num, RANK.prefix); });
                }
            }
        });
    }

    function searchEnglish(query, hits) {
        var index = window.SEARCH_INDEX;
        var lower = query.toLowerCase();
        var words = lower.split(/[\s,;/]+/).map(function(w) {
            return w.replace(/^[()\[\]."'!?:]+|[()\[\]."'!?:]+$/g, '');
        }).filter(function(w) { return w.length > 0 && !STOPWORDS[w]; });
        if (words.length === 0) return;

        var perWord = {};   // num -> number of query words matched (AND)
        var exactAll = {};  // num -> true while every word matched a whole gloss word
        words.forEach(function(word) {
            var matched = {};
            keysOf('english').forEach(function(key) {
                if (key.indexOf(word) !== 0) return;
                idList(index.english[key]).forEach(function(num) {
                    if (!matched[num]) matched[num] = (key === word) ? 'exact' : 'prefix';
                    else if (key === word) matched[num] = 'exact';
                });
            });
            Object.keys(matched).forEach(function(num) {
                perWord[num] = (perWord[num] || 0) + 1;
                if (matched[num] === 'exact') {
                    if (exactAll[num] === undefined) exactAll[num] = true;
                } else {
                    exactAll[num] = false;
                }
            });
        });

        var phrase = lower.replace(/^to\s+/, '').trim();
        Object.keys(perWord).forEach(function(num) {
            if (perWord[num] !== words.length) return;   // AND: every word must match
            var rank = exactAll[num] ? RANK.enWord : RANK.enPrefix;
            var entry = getEntry(num);
            if (entry && exactAll[num]) {
                var phrases = entry.gloss.toLowerCase().split(/[,;]/);
                for (var i = 0; i < phrases.length; i++) {
                    if (phrases[i].replace(/^\s*to\s+/, '').trim() === phrase) { rank = RANK.enPhrase; break; }
                }
            }
            addHit(hits, num, rank);
        });
    }

    function performSearch(query, searchType) {
        if (!window.SEARCH_INDEX) return [];
        var hits = {};
        query = query.trim();

        if (searchType === 'auto') {
            searchType = hasJapanese(query) ? 'japanese' : 'latin';
        }
        if (searchType === 'japanese') {
            searchJapanese(query, hits);
        } else if (searchType === 'romaji') {
            searchRomaji(query, hits);
        } else if (searchType === 'english') {
            searchEnglish(query, hits);
        } else {
            searchRomaji(query, hits);
            searchEnglish(query, hits);
        }

        var results = [];
        Object.keys(hits).forEach(function(num) {
            var entry = getEntry(num);
            if (entry) results.push({ entry: entry, rank: hits[num].rank, form: hits[num].form });
        });
        results.sort(function(a, b) {
            if (a.rank !== b.rank) return a.rank - b.rank;
            var tierDiff = (TIER_RANK[a.entry.tier] || 0) - (TIER_RANK[b.entry.tier] || 0);
            if (tierDiff !== 0) return tierDiff;
            return a.entry.reading.localeCompare(b.entry.reading, 'ja');
        });
        return results;
    }

    // ── Rendering ───────────────────────────────────────────────────────
    function escapeHtml(text) {
        return String(text).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    }

    function renderResult(result) {
        var entry = result.entry;
        var tierName = TIER_NAMES[entry.tier] || 'general';
        var formNote = '';
        if (result.form) {
            formNote = '<div class="result-form-note" lang="ja">' + escapeHtml(result.form) +
                '<span lang="en">: form of </span>' + plainHeadword(entry.headword) + '</div>';
        }
        return '<a href="entries/' + dirRange(entry.id) + '/' + entry.id + '.html" class="result-item">' +
            formNote +
            '<div class="result-headword" lang="ja">' + rubyHtml(entry.headword) + '</div>' +
            '<div class="result-reading" lang="ja">' + entry.reading + '</div>' +
            '<div class="result-gloss">' + entry.gloss + '</div>' +
            '<div class="result-meta">' +
                (entry.pos ? '<span class="result-pos">' + entry.pos + '</span>' : '') +
                '<span class="badge tier-' + tierName + '">' + tierName + '</span>' +
            '</div>' +
        '</a>';
    }

    function showMore() {
        var next = current.results.slice(current.shown, current.shown + PAGE_SIZE);
        resultsList.insertAdjacentHTML('beforeend', next.map(renderResult).join(''));
        current.shown += next.length;
        if (showMoreButton) {
            var remaining = current.results.length - current.shown;
            showMoreButton.style.display = remaining > 0 ? '' : 'none';
            showMoreButton.textContent = 'Show more (' + remaining + ' remaining)';
        }
    }

    function displayResults(query, results) {
        resultsSection.style.display = 'block';
        var introSection = document.getElementById('intro-section');
        if (introSection) introSection.style.display = 'none';

        current = { results: results, shown: 0 };
        resultsList.innerHTML = '';
        if (results.length === 0) {
            resultsHeading.textContent = 'No results for "' + query + '"';
            resultsList.innerHTML = '<p class="no-results">Try a different search term.</p>';
            if (showMoreButton) showMoreButton.style.display = 'none';
        } else {
            resultsHeading.textContent = results.length + ' result' + (results.length === 1 ? '' : 's') + ' for "' + query + '"';
            showMore();
        }
    }

    function selectedType() {
        var checked = document.querySelector('input[name="search-type"]:checked');
        return checked ? checked.value : 'auto';
    }

    function handleSearch() {
        var query = searchInput.value.trim();
        if (!query) return;
        displayResults(query, performSearch(query, selectedType()));
    }

    searchButton.addEventListener('click', handleSearch);
    searchInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') handleSearch();
    });
    if (showMoreButton) showMoreButton.addEventListener('click', showMore);

    // Header search box on this page searches in place
    var headerSearchInput = document.getElementById('header-search-input');
    var headerSearchButton = document.getElementById('header-search-button');
    if (headerSearchInput && headerSearchButton) {
        var handleHeaderSearch = function() {
            var query = headerSearchInput.value.trim();
            if (!query) return;
            searchInput.value = query;
            displayResults(query, performSearch(query, 'auto'));
            headerSearchInput.value = '';
            if (resultsSection) resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
        };
        headerSearchButton.addEventListener('click', handleHeaderSearch);
        headerSearchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') handleHeaderSearch();
        });
    }

    // ?q=...&type=... (from the header search box on other pages)
    function handleUrlParams() {
        var params = new URLSearchParams(window.location.search);
        var query = params.get('q');
        var searchType = params.get('type') || 'auto';
        if (!query) return;

        searchInput.value = query;
        var radio = document.querySelector('input[name="search-type"][value="' + searchType + '"]');
        if (radio) radio.checked = true; else searchType = 'auto';
        displayResults(query, performSearch(query, searchType));

        if (window.history.replaceState) {
            window.history.replaceState({}, document.title, window.location.pathname);
        }
    }

    if (window.SEARCH_INDEX) {
        handleUrlParams();
    } else {
        var checkInterval = setInterval(function() {
            if (window.SEARCH_INDEX) {
                clearInterval(checkInterval);
                handleUrlParams();
            }
        }, 50);
        setTimeout(function() { clearInterval(checkInterval); }, 5000);
    }
})();
