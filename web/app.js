/**
 * Japanese-English Learner's Dictionary Web Application
 * A static dictionary with Search, Browse, and Compare interfaces
 */

(function() {
    'use strict';

    // State
    let entriesData = null;
    let indexData = null;
    let isLoaded = false;
    let furiganaEnabled = false;
    let currentInterface = 'search';

    // Browse state
    let browseFilters = {
        jlpt: 'all',
        pos: 'all',
        kana: 'all'
    };

    // Pattern to match furigana notation: {kanji|reading}
    const FURIGANA_PATTERN = /\{([^|]+)\|([^}]+)\}/g;

    // Kana row definitions
    const KANA_ROWS = [
        { name: 'あ行', kana: 'あいうえお', key: 'あ' },
        { name: 'か行', kana: 'かきくけこがぎぐげご', key: 'か' },
        { name: 'さ行', kana: 'さしすせそざじずぜぞ', key: 'さ' },
        { name: 'た行', kana: 'たちつてとだぢづでど', key: 'た' },
        { name: 'な行', kana: 'なにぬねの', key: 'な' },
        { name: 'は行', kana: 'はひふへほばびぶべぼぱぴぷぺぽ', key: 'は' },
        { name: 'ま行', kana: 'まみむめも', key: 'ま' },
        { name: 'や行', kana: 'やゆよ', key: 'や' },
        { name: 'ら行', kana: 'らりるれろ', key: 'ら' },
        { name: 'わ行', kana: 'わをん', key: 'わ' },
    ];

    // Comparison groups for the Compare interface
    const COMPARISON_GROUPS = {
        particles: [
            { label: 'は vs が', entries: ['wa', 'ga'] },
            { label: 'に vs で', entries: ['ni', 'de'] },
            { label: 'を vs に', entries: ['wo', 'ni'] },
            { label: 'から vs まで', entries: ['kara', 'made'] },
            { label: 'と vs や', entries: ['to', 'ya'] },
        ],
        transitive: [
            { label: '開ける vs 開く', entries: ['akeru', 'aku'] },
            { label: '閉める vs 閉まる', entries: ['shimeru', 'shimaru'] },
            { label: '付ける vs 付く', entries: ['tsukeru', 'tsuku'] },
            { label: '消す vs 消える', entries: ['kesu', 'kieru'] },
            { label: '入れる vs 入る', entries: ['ireru', 'hairu'] },
            { label: '出す vs 出る', entries: ['dasu', 'deru'] },
            { label: '起こす vs 起きる', entries: ['okosu', 'okiru'] },
            { label: '落とす vs 落ちる', entries: ['otosu', 'ochiru'] },
            { label: '壊す vs 壊れる', entries: ['kowasu', 'kowareru'] },
            { label: '直す vs 直る', entries: ['naosu', 'naoru'] },
        ],
        similar: [
            { label: '見る vs 見える vs 見せる', entries: ['miru', 'mieru', 'miseru'] },
            { label: '聞く vs 聞こえる', entries: ['kiku', 'kikoeru'] },
            { label: 'きれい vs 美しい', entries: ['kirei', 'utsukushii'] },
            { label: '大きい vs 大きな', entries: ['ookii', 'ookina'] },
            { label: '思う vs 考える', entries: ['omou', 'kangaeru'] },
            { label: '分かる vs 知る', entries: ['wakaru', 'shiru'] },
            { label: 'いる vs ある', entries: ['iru', 'aru'] },
            { label: '行く vs 来る', entries: ['iku', 'kuru'] },
        ]
    };

    // DOM Elements - Search Interface
    const searchForm = document.getElementById('search-form');
    const searchInput = document.getElementById('search-input');
    const resultsSection = document.getElementById('results-section');
    const resultsHeading = document.getElementById('results-heading');
    const resultsList = document.getElementById('results-list');
    const entrySection = document.getElementById('entry-section');
    const entryDisplay = document.getElementById('entry-display');
    const welcomeSection = document.getElementById('welcome-section');
    const statsDiv = document.getElementById('stats');
    const entryBrowser = document.getElementById('entry-browser');

    // DOM Elements - Browse Interface
    const browseList = document.getElementById('browse-list');
    const browseHeading = document.getElementById('browse-heading');
    const browseCount = document.getElementById('browse-count');
    const browseEntryDisplay = document.getElementById('browse-entry-display');

    // DOM Elements - Compare Interface
    const particleComparisons = document.getElementById('particle-comparisons');
    const transitiveComparisons = document.getElementById('transitive-comparisons');
    const similarComparisons = document.getElementById('similar-comparisons');
    const compareCategories = document.getElementById('compare-categories');
    const compareDisplay = document.getElementById('compare-display');
    const compareCards = document.getElementById('compare-cards');
    const compareBack = document.getElementById('compare-back');

    /**
     * Get the kana row for a reading based on its first character
     */
    function getKanaRow(reading) {
        if (!reading) return null;
        const firstChar = reading[0];
        for (const row of KANA_ROWS) {
            if (row.kana.includes(firstChar)) {
                return row;
            }
        }
        return null;
    }

    /**
     * Get part of speech category
     */
    function getPosCategory(pos) {
        if (!pos) return 'other';
        const posLower = pos.toLowerCase();
        // Check adverb before verb since "adverb" contains "verb"
        if (posLower.includes('adverb')) return 'adverb';
        if (posLower.includes('verb')) return 'verb';
        if (posLower.includes('noun')) return 'noun';
        if (posLower.includes('adjective')) return 'adjective';
        if (posLower.includes('particle')) return 'particle';
        if (posLower.includes('counter')) return 'counter';
        return 'other';
    }

    /**
     * Build the sidebar entry browser for Search interface
     */
    function buildEntryBrowser() {
        if (!entriesData || !entriesData.entries) {
            entryBrowser.innerHTML = '<p class="no-entries">No entries available</p>';
            return;
        }

        const grouped = {};
        for (const row of KANA_ROWS) {
            grouped[row.name] = [];
        }

        const entries = Object.values(entriesData.entries);
        for (const entry of entries) {
            const row = getKanaRow(entry.reading);
            if (row && grouped[row.name]) {
                grouped[row.name].push(entry);
            }
        }

        for (const rowName of Object.keys(grouped)) {
            grouped[rowName].sort((a, b) => a.reading.localeCompare(b.reading, 'ja'));
        }

        let html = '';
        for (const row of KANA_ROWS) {
            const entries = grouped[row.name];
            if (entries.length === 0) continue;

            html += `
                <div class="kana-group">
                    <div class="kana-group-header">${row.name}</div>
                    <div class="kana-group-entries">
            `;

            for (const entry of entries) {
                html += `
                    <a class="browser-entry" data-entry-id="${entry.id}">
                        <span class="browser-entry-headword">${processJapaneseText(entry.headword)}</span>
                        <span class="browser-entry-meta">
                            <span class="browser-entry-reading">${escapeHtml(entry.reading)}</span>
                        </span>
                    </a>
                `;
            }

            html += `
                    </div>
                </div>
            `;
        }

        entryBrowser.innerHTML = html;

        entryBrowser.querySelectorAll('.browser-entry').forEach(item => {
            item.addEventListener('click', (e) => {
                e.preventDefault();
                const entryId = item.dataset.entryId;
                displayEntry(entryId);
            });
        });
    }

    /**
     * Initialize the application
     */
    function init() {
        loadFuriganaPreference();
        loadInterfacePreference();

        // Set up furigana toggle button
        const furiganaBtn = document.getElementById('furigana-toggle');
        if (furiganaBtn) {
            furiganaBtn.addEventListener('click', toggleFurigana);
        }

        // Set up interface toggle buttons
        document.querySelectorAll('.interface-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                switchInterface(btn.dataset.interface);
            });
        });

        // Load dictionary data
        if (typeof DICTIONARY_DATA !== 'undefined' && typeof DICTIONARY_INDEX !== 'undefined') {
            entriesData = DICTIONARY_DATA;
            indexData = DICTIONARY_INDEX;
            isLoaded = true;

            const count = entriesData.count;
            statsDiv.textContent = `${count} ${count === 1 ? 'entry' : 'entries'} available`;

            buildEntryBrowser();
            initBrowseInterface();
            initCompareInterface();
            updateLastUpdated();

            console.log('Dictionary loaded:', entriesData.count, 'entries');
        } else {
            console.error('Dictionary data not found.');
            statsDiv.textContent = 'Error: Dictionary data not found.';
        }

        // Set up search form
        searchForm.addEventListener('submit', handleSearch);

        // Set up browse filters
        setupBrowseFilters();

        // Set up compare back button
        if (compareBack) {
            compareBack.addEventListener('click', () => {
                compareCategories.classList.remove('hidden');
                compareDisplay.classList.add('hidden');
            });
        }
    }

    /**
     * Switch between interfaces
     */
    function switchInterface(interfaceName) {
        currentInterface = interfaceName;

        // Update buttons
        document.querySelectorAll('.interface-btn').forEach(btn => {
            btn.classList.toggle('active', btn.dataset.interface === interfaceName);
        });

        // Update panels
        document.querySelectorAll('.interface-panel').forEach(panel => {
            panel.classList.toggle('active', panel.id === `interface-${interfaceName}`);
        });

        // Save preference
        try {
            localStorage.setItem('interface-preference', interfaceName);
        } catch (e) {}
    }

    /**
     * Load interface preference
     */
    function loadInterfacePreference() {
        try {
            const saved = localStorage.getItem('interface-preference');
            if (saved && ['search', 'browse', 'compare'].includes(saved)) {
                switchInterface(saved);
            }
        } catch (e) {}
    }

    /**
     * Handle search form submission
     */
    function handleSearch(event) {
        event.preventDefault();

        if (!isLoaded) {
            alert('Dictionary is still loading. Please wait.');
            return;
        }

        const query = searchInput.value.trim();
        if (!query) return;

        const searchType = document.querySelector('input[name="search-type"]:checked').value;
        const results = performSearch(query, searchType);
        displayResults(query, results);
    }

    /**
     * Detect the type of search query
     */
    function detectQueryType(query) {
        if (/[\u3040-\u309f\u30a0-\u30ff\u4e00-\u9faf]/.test(query)) {
            return 'japanese';
        }
        if (/^[a-z]+$/i.test(query)) {
            return query.length <= 10 ? 'romaji' : 'english';
        }
        return 'english';
    }

    /**
     * Perform search based on query and type
     */
    function performSearch(query, searchType) {
        const index = indexData.index;
        let entryIds = new Set();

        if (searchType === 'auto') {
            searchType = detectQueryType(query);
        }

        const queryLower = query.toLowerCase();

        switch (searchType) {
            case 'japanese':
                if (index.japanese[query]) {
                    index.japanese[query].forEach(id => entryIds.add(id));
                }
                Object.keys(index.japanese).forEach(key => {
                    if (key.includes(query) && key !== query) {
                        index.japanese[key].forEach(id => entryIds.add(id));
                    }
                });
                break;

            case 'romaji':
                if (index.romaji[queryLower]) {
                    index.romaji[queryLower].forEach(id => entryIds.add(id));
                }
                Object.keys(index.romaji).forEach(key => {
                    if (key.startsWith(queryLower) && key !== queryLower) {
                        index.romaji[key].forEach(id => entryIds.add(id));
                    }
                });
                break;

            case 'english':
                const words = queryLower.split(/\s+/);
                words.forEach(word => {
                    if (index.english[word]) {
                        index.english[word].forEach(id => entryIds.add(id));
                    }
                    Object.keys(index.english).forEach(key => {
                        if (key.startsWith(word) && key !== word) {
                            index.english[key].forEach(id => entryIds.add(id));
                        }
                    });
                });
                break;
        }

        const results = [];
        entryIds.forEach(id => {
            if (entriesData.entries[id]) {
                results.push(entriesData.entries[id]);
            }
        });

        results.sort((a, b) => a.reading.localeCompare(b.reading, 'ja'));
        return results;
    }

    /**
     * Display search results
     */
    function displayResults(query, results) {
        welcomeSection.classList.add('hidden');
        entrySection.classList.add('hidden');

        if (results.length === 0) {
            resultsHeading.textContent = `No results for "${query}"`;
            resultsList.innerHTML = '<p class="no-results">Try a different search term or check your spelling.</p>';
        } else {
            resultsHeading.textContent = `${results.length} result${results.length === 1 ? '' : 's'} for "${query}"`;
            resultsList.innerHTML = results.map(entry => createResultItem(entry)).join('');

            resultsList.querySelectorAll('.result-item').forEach(item => {
                item.addEventListener('click', () => {
                    const entryId = item.dataset.entryId;
                    displayEntry(entryId);
                });
            });
        }

        resultsSection.classList.remove('hidden');
    }

    /**
     * Create HTML for a result item
     */
    function createResultItem(entry) {
        return `
            <div class="result-item" data-entry-id="${entry.id}">
                <div>
                    <span class="headword">${processJapaneseText(entry.headword)}</span>
                    <span class="reading">${escapeHtml(entry.reading)}</span>
                </div>
                <div class="gloss">${escapeHtml(entry.gloss)}</div>
            </div>
        `;
    }

    /**
     * Display a full entry in the Search interface
     */
    function displayEntry(entryId) {
        const entry = entriesData.entries[entryId];
        if (!entry) {
            console.error('Entry not found:', entryId);
            return;
        }

        entryDisplay.dataset.currentEntryId = entryId;
        entryDisplay.innerHTML = createEntryDisplay(entry);
        entrySection.classList.remove('hidden');
        entrySection.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    /**
     * Create HTML for full entry display
     */
    function createEntryDisplay(entry) {
        let html = `
            <div class="entry-header">
                <div class="entry-headword">${processJapaneseText(entry.headword)}</div>
                <div class="entry-reading">${escapeHtml(entry.reading)}</div>
                <div class="entry-pos">${escapeHtml(entry.part_of_speech)}</div>
                <div class="entry-gloss">${escapeHtml(entry.gloss)}</div>
            </div>
        `;

        if (entry.definitions && entry.definitions.length > 0) {
            html += `<div class="definitions"><h3>Definitions</h3>`;
            entry.definitions.forEach(def => {
                html += `
                    <div class="definition-item">
                        <span class="definition-number">${def.sense_number}.</span>
                        <span class="definition-gloss">${escapeHtml(def.gloss)}</span>
                        ${def.explanation ? `<div class="definition-explanation">${processJapaneseText(def.explanation)}</div>` : ''}
                    </div>
                `;
            });
            html += `</div>`;
        }

        if (entry.examples && entry.examples.length > 0) {
            html += `<div class="examples"><h3>Examples</h3>`;
            entry.examples.forEach(ex => {
                html += `
                    <div class="example-item">
                        <div class="example-japanese">${processJapaneseText(ex.japanese)}</div>
                        <div class="example-english">${escapeHtml(ex.english)}</div>
                        ${ex.notes ? `<div class="example-notes">${processJapaneseText(ex.notes)}</div>` : ''}
                    </div>
                `;
            });
            html += `</div>`;
        }

        if (entry.notes) {
            html += `
                <div class="entry-notes">
                    <h3>Notes</h3>
                    <div class="notes-content">${processNotesText(entry.notes)}</div>
                </div>
            `;
        }

        html += `
            <div class="entry-metadata">
                <div class="metadata-badges">
                    ${entry.metadata.jlpt_level ? `<span class="badge jlpt">${entry.metadata.jlpt_level}</span>` : ''}
                    <span class="badge status-${entry.metadata.review_status}">${entry.metadata.review_status}</span>
                </div>
            </div>
        `;

        return html;
    }

    // ===== BROWSE INTERFACE =====

    /**
     * Initialize the Browse interface
     */
    function initBrowseInterface() {
        updateBrowseList();
    }

    /**
     * Set up browse filter event handlers
     */
    function setupBrowseFilters() {
        // JLPT filters
        document.querySelectorAll('#jlpt-filters .filter-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                document.querySelectorAll('#jlpt-filters .filter-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                browseFilters.jlpt = btn.dataset.jlpt;
                updateBrowseList();
            });
        });

        // POS filters
        document.querySelectorAll('#pos-filters .filter-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                document.querySelectorAll('#pos-filters .filter-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                browseFilters.pos = btn.dataset.pos;
                updateBrowseList();
            });
        });

        // Kana filters
        document.querySelectorAll('#kana-filters .filter-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                document.querySelectorAll('#kana-filters .filter-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                browseFilters.kana = btn.dataset.kana;
                updateBrowseList();
            });
        });
    }

    /**
     * Update the browse list based on current filters
     */
    function updateBrowseList() {
        if (!entriesData || !entriesData.entries) return;

        let entries = Object.values(entriesData.entries);

        // Apply JLPT filter
        if (browseFilters.jlpt !== 'all') {
            entries = entries.filter(e => e.metadata.jlpt_level === browseFilters.jlpt);
        }

        // Apply POS filter
        if (browseFilters.pos !== 'all') {
            entries = entries.filter(e => getPosCategory(e.part_of_speech) === browseFilters.pos);
        }

        // Apply kana filter
        if (browseFilters.kana !== 'all') {
            entries = entries.filter(e => {
                const row = getKanaRow(e.reading);
                return row && row.key === browseFilters.kana;
            });
        }

        // Sort by reading
        entries.sort((a, b) => a.reading.localeCompare(b.reading, 'ja'));

        // Update heading
        let headingParts = [];
        if (browseFilters.jlpt !== 'all') headingParts.push(browseFilters.jlpt);
        if (browseFilters.pos !== 'all') headingParts.push(browseFilters.pos + 's');
        if (browseFilters.kana !== 'all') {
            const row = KANA_ROWS.find(r => r.key === browseFilters.kana);
            if (row) headingParts.push(row.name);
        }
        browseHeading.textContent = headingParts.length > 0 ? headingParts.join(' - ') : 'All Entries';
        browseCount.textContent = `${entries.length} entries`;

        // Build list
        let html = '';
        for (const entry of entries) {
            html += `
                <div class="browse-item" data-entry-id="${entry.id}">
                    <span class="browse-item-headword">${processJapaneseText(entry.headword)}</span>
                    <span class="browse-item-reading">${escapeHtml(entry.reading)}</span>
                </div>
            `;
        }

        browseList.innerHTML = html || '<p class="browse-placeholder">No entries match the selected filters</p>';

        // Add click handlers
        browseList.querySelectorAll('.browse-item').forEach(item => {
            item.addEventListener('click', () => {
                browseList.querySelectorAll('.browse-item').forEach(i => i.classList.remove('active'));
                item.classList.add('active');
                displayBrowseEntry(item.dataset.entryId);
            });
        });
    }

    /**
     * Display an entry in the Browse interface detail panel
     */
    function displayBrowseEntry(entryId) {
        const entry = entriesData.entries[entryId];
        if (!entry) return;

        browseEntryDisplay.innerHTML = createEntryDisplay(entry);
    }

    // ===== COMPARE INTERFACE =====

    /**
     * Initialize the Compare interface
     */
    function initCompareInterface() {
        buildCompareButtons(particleComparisons, COMPARISON_GROUPS.particles);
        buildCompareButtons(transitiveComparisons, COMPARISON_GROUPS.transitive);
        buildCompareButtons(similarComparisons, COMPARISON_GROUPS.similar);
    }

    /**
     * Build comparison buttons for a category
     */
    function buildCompareButtons(container, groups) {
        if (!container) return;

        let html = '';
        for (const group of groups) {
            // Check if entries exist
            const entriesExist = group.entries.every(romaji => findEntryByRomaji(romaji));
            if (entriesExist) {
                html += `<button class="compare-btn" data-entries="${group.entries.join(',')}">${group.label}</button>`;
            }
        }

        container.innerHTML = html || '<p class="browse-placeholder">No comparisons available</p>';

        // Add click handlers
        container.querySelectorAll('.compare-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const entryRomajis = btn.dataset.entries.split(',');
                showComparison(entryRomajis);
            });
        });
    }

    /**
     * Find an entry by its romaji (approximate match)
     */
    function findEntryByRomaji(romaji) {
        if (!indexData || !indexData.index || !indexData.index.romaji) return null;

        const ids = indexData.index.romaji[romaji];
        if (ids && ids.length > 0) {
            return entriesData.entries[ids[0]];
        }
        return null;
    }

    /**
     * Show comparison cards for selected entries
     */
    function showComparison(romajis) {
        const entries = romajis.map(r => findEntryByRomaji(r)).filter(e => e);

        if (entries.length === 0) {
            alert('Could not find entries for comparison.');
            return;
        }

        compareCategories.classList.add('hidden');
        compareDisplay.classList.remove('hidden');

        let html = '';
        for (const entry of entries) {
            html += `<div class="compare-card">${createEntryDisplay(entry)}</div>`;
        }

        compareCards.innerHTML = html;
    }

    // ===== UTILITY FUNCTIONS =====

    /**
     * Escape HTML special characters
     */
    function escapeHtml(text) {
        if (!text) return '';
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    /**
     * Process Japanese text with furigana notation
     */
    function processJapaneseText(text) {
        if (!text) return '';

        const parts = [];
        let lastIndex = 0;
        let match;

        FURIGANA_PATTERN.lastIndex = 0;

        while ((match = FURIGANA_PATTERN.exec(text)) !== null) {
            if (match.index > lastIndex) {
                parts.push(escapeHtml(text.slice(lastIndex, match.index)));
            }

            const kanji = match[1];
            const reading = match[2];

            if (furiganaEnabled) {
                parts.push(`<ruby>${escapeHtml(kanji)}<rp>(</rp><rt>${escapeHtml(reading)}</rt><rp>)</rp></ruby>`);
            } else {
                parts.push(escapeHtml(kanji));
            }

            lastIndex = match.index + match[0].length;
        }

        if (lastIndex < text.length) {
            parts.push(escapeHtml(text.slice(lastIndex)));
        }

        return parts.join('');
    }

    /**
     * Process notes text with proper formatting
     */
    function processNotesText(text) {
        if (!text) return '';

        const paragraphs = text.split(/\n\n+/);

        return paragraphs.map(para => {
            const lines = para.split('\n');
            const hasBullets = lines.some(line => line.trim().startsWith('- ') || line.trim().startsWith('・'));

            if (hasBullets) {
                let html = '';
                let listItems = [];

                lines.forEach(line => {
                    const trimmed = line.trim();
                    if (trimmed.startsWith('- ') || trimmed.startsWith('・')) {
                        const content = trimmed.replace(/^[-・]\s*/, '');
                        listItems.push(`<li>${processJapaneseText(content)}</li>`);
                    } else if (trimmed) {
                        if (listItems.length > 0) {
                            html += `<ul>${listItems.join('')}</ul>`;
                            listItems = [];
                        }
                        html += `<p>${processJapaneseText(trimmed)}</p>`;
                    }
                });

                if (listItems.length > 0) {
                    html += `<ul>${listItems.join('')}</ul>`;
                }

                return html;
            } else {
                const processed = lines
                    .map(line => processJapaneseText(line.trim()))
                    .filter(line => line)
                    .join('<br>');
                return `<p>${processed}</p>`;
            }
        }).join('');
    }

    /**
     * Toggle furigana visibility
     */
    function toggleFurigana() {
        furiganaEnabled = !furiganaEnabled;

        const btn = document.getElementById('furigana-toggle');
        if (btn) {
            btn.classList.toggle('active', furiganaEnabled);
            btn.setAttribute('aria-pressed', furiganaEnabled);
        }

        try {
            localStorage.setItem('furigana-enabled', furiganaEnabled);
        } catch (e) {}

        // Re-render all interfaces
        buildEntryBrowser();
        updateBrowseList();

        // Re-render current entry in search
        if (!entrySection.classList.contains('hidden')) {
            const currentEntryId = entryDisplay.dataset.currentEntryId;
            if (currentEntryId && entriesData.entries[currentEntryId]) {
                displayEntry(currentEntryId);
            }
        }

        // Re-render search results
        if (!resultsSection.classList.contains('hidden')) {
            resultsList.querySelectorAll('.result-item').forEach(item => {
                const entryId = item.dataset.entryId;
                const entry = entriesData.entries[entryId];
                if (entry) {
                    item.querySelector('.headword').innerHTML = processJapaneseText(entry.headword);
                }
            });
        }

        // Re-render browse entry display
        const browseActiveItem = browseList.querySelector('.browse-item.active');
        if (browseActiveItem) {
            displayBrowseEntry(browseActiveItem.dataset.entryId);
        }

        // Re-render compare cards
        if (!compareDisplay.classList.contains('hidden')) {
            compareCards.querySelectorAll('.compare-card').forEach(card => {
                const headword = card.querySelector('.entry-headword');
                if (headword) {
                    // Find entry by headword text and re-render
                    const entryId = card.querySelector('.metadata-badges')?.closest('.compare-card')?.dataset?.entryId;
                    // Simplified: just toggle existing ruby elements
                }
            });
        }
    }

    /**
     * Load furigana preference from localStorage
     */
    function loadFuriganaPreference() {
        try {
            const saved = localStorage.getItem('furigana-enabled');
            if (saved !== null) {
                furiganaEnabled = saved === 'true';
            }
        } catch (e) {}

        const btn = document.getElementById('furigana-toggle');
        if (btn) {
            btn.classList.toggle('active', furiganaEnabled);
            btn.setAttribute('aria-pressed', furiganaEnabled);
        }
    }

    /**
     * Update the last updated date in the footer
     */
    function updateLastUpdated() {
        const lastUpdatedEl = document.getElementById('last-updated');
        if (!lastUpdatedEl || !entriesData || !entriesData.entries) return;

        // Find the most recent modification date
        let latestDate = null;
        for (const entry of Object.values(entriesData.entries)) {
            if (entry.metadata && entry.metadata.modified) {
                const date = new Date(entry.metadata.modified);
                if (!latestDate || date > latestDate) {
                    latestDate = date;
                }
            }
        }

        if (latestDate) {
            const formatted = latestDate.toLocaleDateString('en-US', {
                year: 'numeric',
                month: 'long',
                day: 'numeric'
            });
            lastUpdatedEl.textContent = `Last updated: ${formatted}`;
        }
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
