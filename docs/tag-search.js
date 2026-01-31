/**
 * Tag-Based Search functionality for je-dict-1 dictionary
 * Provides filtering by tags, statistics, missing tag detection, and combined queries
 */
(function() {
    'use strict';

    const RESULTS_PER_PAGE = 50;
    const VERB_POS_TAGS = ['verb-godan', 'verb-ichidan', 'verb-suru', 'verb-kuru', 'verb-irregular'];

    let currentResults = [];
    let currentPage = 1;
    let currentMode = 'filter';

    const filterPanel = document.getElementById('filter-panel');
    const statsPanel = document.getElementById('stats-panel');
    const missingPanel = document.getElementById('missing-panel');
    const combinedPanel = document.getElementById('combined-panel');
    const resultsContainer = document.getElementById('tag-results');
    const resultsCountEl = document.getElementById('tag-results-count');
    const resultsListEl = document.getElementById('tag-results-list');
    const paginationEl = document.getElementById('tag-pagination');

    function getAllEntries() {
        if (!window.SEARCH_ENTRIES) return [];
        return Object.values(window.SEARCH_ENTRIES);
    }

    function entryHasTag(entry, category, value) {
        const tags = entry.tags || {};
        if (value === '_missing') {
            if (category === 'transitivity') {
                const pos = tags.pos || [];
                const isVerb = VERB_POS_TAGS.some(v => pos.includes(v));
                return isVerb && !tags.transitivity;
            }
            return false;
        }
        if (category === 'tier') {
            return entry.tier === value;
        }
        const tagValue = tags[category];
        if (Array.isArray(tagValue)) {
            return tagValue.includes(value);
        } else if (typeof tagValue === 'string') {
            return tagValue === value;
        }
        return false;
    }

    function entryMissingTag(entry, category) {
        const tags = entry.tags || {};
        if (category === 'pos') return !tags.pos || tags.pos.length === 0;
        if (category === 'formality') return !tags.formality;
        if (category === 'politeness') return !tags.politeness;
        if (category === 'semantic') return !tags.semantic || tags.semantic.length === 0;
        if (category === 'transitivity') {
            const pos = tags.pos || [];
            const isVerb = VERB_POS_TAGS.some(v => pos.includes(v));
            return isVerb && !tags.transitivity;
        }
        return false;
    }

    function getSelectedFilters() {
        const filters = {};
        const categories = ['tier', 'pos', 'transitivity', 'formality', 'politeness', 'semantic', 'style', 'domain'];
        categories.forEach(category => {
            const checked = document.querySelectorAll('input[name="' + category + '"]:checked');
            if (checked.length > 0) {
                filters[category] = Array.from(checked).map(el => el.value);
            }
        });
        return filters;
    }

    function filterEntries(entries, filters, andMode) {
        if (Object.keys(filters).length === 0) return entries;
        return entries.filter(entry => {
            if (andMode) {
                return Object.entries(filters).every(([category, values]) => {
                    return values.some(value => entryHasTag(entry, category, value));
                });
            } else {
                return Object.entries(filters).some(([category, values]) => {
                    return values.some(value => entryHasTag(entry, category, value));
                });
            }
        });
    }

    function applyFilters() {
        const filters = getSelectedFilters();
        const andMode = document.getElementById('filter-and-mode').checked;
        const entries = getAllEntries();
        currentResults = filterEntries(entries, filters, andMode);
        currentResults.sort((a, b) => a.reading.localeCompare(b.reading, 'ja'));
        currentPage = 1;
        displayResults();
    }

    function findMissingTags() {
        const checked = document.querySelectorAll('input[name="missing"]:checked');
        const categories = Array.from(checked).map(el => el.value);
        if (categories.length === 0) {
            alert('Please select at least one tag category.');
            return;
        }
        const entries = getAllEntries();
        currentResults = entries.filter(entry => {
            return categories.some(category => entryMissingTag(entry, category));
        });
        currentResults.sort((a, b) => a.reading.localeCompare(b.reading, 'ja'));
        currentPage = 1;
        displayResults();
    }

    function runCombinedQuery() {
        const queryInput = document.getElementById('query-input');
        const query = queryInput.value.trim();
        if (!query) {
            alert('Please enter a query.');
            return;
        }
        try {
            const entries = getAllEntries();
            currentResults = executeQuery(entries, query);
            currentResults.sort((a, b) => a.reading.localeCompare(b.reading, 'ja'));
            currentPage = 1;
            displayResults();
        } catch (e) {
            alert('Query error: ' + e.message);
        }
    }

    function executeQuery(entries, query) {
        const orParts = query.split(/\s+OR\s+/i);
        return entries.filter(entry => {
            return orParts.some(orPart => {
                const andParts = orPart.split(/\s+AND\s+/i);
                return andParts.every(andPart => {
                    const trimmed = andPart.trim();
                    const isNegated = trimmed.startsWith('NOT ');
                    const condition = isNegated ? trimmed.substring(4).trim() : trimmed;
                    const match = condition.match(/^(\w+):(.+)$/);
                    if (!match) throw new Error('Invalid condition: ' + condition);
                    const [, category, value] = match;
                    let result;
                    if (value === '*') {
                        const tags = entry.tags || {};
                        if (category === 'tier') {
                            result = !!entry.tier;
                        } else if (Array.isArray(tags[category])) {
                            result = tags[category].length > 0;
                        } else {
                            result = !!tags[category];
                        }
                    } else {
                        result = entryHasTag(entry, category, value);
                    }
                    return isNegated ? !result : result;
                });
            });
        });
    }

    function displayResults() {
        resultsContainer.style.display = 'block';
        const total = currentResults.length;
        const totalPages = Math.ceil(total / RESULTS_PER_PAGE);
        const start = (currentPage - 1) * RESULTS_PER_PAGE;
        const end = Math.min(start + RESULTS_PER_PAGE, total);
        const pageResults = currentResults.slice(start, end);

        if (total === 0) {
            resultsCountEl.textContent = '0 entries found';
        } else {
            resultsCountEl.textContent = total + ' entries found (showing ' + (start + 1) + '-' + end + ')';
        }

        resultsListEl.innerHTML = pageResults.map(entry => {
            const tags = entry.tags || {};
            const posStr = (tags.pos || []).join(', ');
            const semanticStr = (tags.semantic || []).slice(0, 3).join(', ');
            const tagSummary = [posStr, tags.formality, semanticStr].filter(Boolean).join(' | ');
            return '<a href="entries/' + entry.dirRange + '/' + entry.id + '.html" class="tag-result-item">' +
                '<div class="tag-result-headword">' + entry.headword + '</div>' +
                '<div class="tag-result-reading">' + entry.reading + '</div>' +
                '<div class="tag-result-gloss">' + entry.gloss + '</div>' +
                '<div class="tag-result-tags">' + tagSummary + '</div>' +
            '</a>';
        }).join('');

        renderPagination(totalPages);
    }

    function renderPagination(totalPages) {
        if (totalPages <= 1) {
            paginationEl.innerHTML = '';
            return;
        }
        let html = '<button ' + (currentPage === 1 ? 'disabled' : '') + ' data-page="' + (currentPage - 1) + '">← Prev</button>';
        const pages = [1];
        if (currentPage > 3) pages.push('...');
        for (let i = Math.max(2, currentPage - 1); i <= Math.min(totalPages - 1, currentPage + 1); i++) {
            pages.push(i);
        }
        if (currentPage < totalPages - 2) pages.push('...');
        if (totalPages > 1) pages.push(totalPages);
        pages.forEach(p => {
            if (p === '...') {
                html += '<span class="page-info">...</span>';
            } else {
                html += '<button ' + (p === currentPage ? 'class="current"' : '') + ' data-page="' + p + '">' + p + '</button>';
            }
        });
        html += '<button ' + (currentPage === totalPages ? 'disabled' : '') + ' data-page="' + (currentPage + 1) + '">Next →</button>';
        paginationEl.innerHTML = html;
    }

    function calculateStats() {
        const entries = getAllEntries();
        const stats = { total: entries.length, tier: {}, pos: {}, transitivity: {}, formality: {}, politeness: {}, semantic: {}, style: {}, domain: {} };
        let verbCount = 0;

        entries.forEach(entry => {
            const tags = entry.tags || {};
            const tier = entry.tier || 'unknown';
            stats.tier[tier] = (stats.tier[tier] || 0) + 1;
            const pos = tags.pos || [];
            pos.forEach(p => { stats.pos[p] = (stats.pos[p] || 0) + 1; });
            const isVerb = VERB_POS_TAGS.some(v => pos.includes(v));
            if (isVerb) verbCount++;
            if (isVerb) {
                const trans = tags.transitivity || '(missing)';
                stats.transitivity[trans] = (stats.transitivity[trans] || 0) + 1;
            }
            const formality = tags.formality || '(missing)';
            stats.formality[formality] = (stats.formality[formality] || 0) + 1;
            const politeness = tags.politeness || '(missing)';
            stats.politeness[politeness] = (stats.politeness[politeness] || 0) + 1;
            const semantic = tags.semantic || [];
            if (semantic.length === 0) {
                stats.semantic['(missing)'] = (stats.semantic['(missing)'] || 0) + 1;
            } else {
                semantic.forEach(s => { stats.semantic[s] = (stats.semantic[s] || 0) + 1; });
            }
            (tags.style || []).forEach(s => { stats.style[s] = (stats.style[s] || 0) + 1; });
            (tags.domain || []).forEach(d => { stats.domain[d] = (stats.domain[d] || 0) + 1; });
        });

        const statsGrid = document.getElementById('stats-grid');
        statsGrid.innerHTML = '<div class="stats-card"><h3>Overview</h3>' +
            '<div class="stats-item"><span>Total entries</span><span class="stats-value">' + stats.total + '</span></div>' +
            '<div class="stats-item"><span>Verb entries</span><span class="stats-value">' + verbCount + '</span></div></div>' +
            '<div class="stats-card"><h3>Vocabulary Tier</h3>' + renderStatsItems(stats.tier, stats.total) + '</div>' +
            '<div class="stats-card"><h3>Part of Speech (top 15)</h3>' + renderStatsItems(stats.pos, stats.total, 15) + '</div>' +
            '<div class="stats-card"><h3>Transitivity (' + verbCount + ' verbs)</h3>' + renderStatsItems(stats.transitivity, verbCount) + '</div>' +
            '<div class="stats-card"><h3>Formality</h3>' + renderStatsItems(stats.formality, stats.total) + '</div>' +
            '<div class="stats-card"><h3>Politeness</h3>' + renderStatsItems(stats.politeness, stats.total) + '</div>' +
            '<div class="stats-card"><h3>Semantic (top 20)</h3>' + renderStatsItems(stats.semantic, stats.total, 20) + '</div>' +
            '<div class="stats-card"><h3>Style</h3>' + renderStatsItems(stats.style, stats.total) + '</div>' +
            '<div class="stats-card"><h3>Domain</h3>' + renderStatsItems(stats.domain, stats.total) + '</div>';
    }

    function renderStatsItems(data, total, limit) {
        const entries = Object.entries(data).sort((a, b) => b[1] - a[1]);
        const displayEntries = limit ? entries.slice(0, limit) : entries;
        if (displayEntries.length === 0) return '<div class="stats-item"><span>(no data)</span></div>';
        return displayEntries.map(([key, count]) => {
            const pct = (count / total * 100).toFixed(1);
            return '<div class="stats-item"><span>' + key + '</span><span class="stats-value">' + count + ' (' + pct + '%)' +
                '<span class="stats-bar"><span class="stats-bar-fill" style="width:' + pct + '%"></span></span></span></div>';
        }).join('');
    }

    function exportCSV() {
        if (currentResults.length === 0) { alert('No results to export.'); return; }
        const headers = ['id', 'headword', 'reading', 'gloss', 'tier', 'pos', 'formality', 'politeness', 'transitivity', 'semantic', 'style', 'domain'];
        const rows = currentResults.map(entry => {
            const tags = entry.tags || {};
            return [entry.id, entry.headword.replace(/<[^>]+>/g, ''), entry.reading, entry.gloss, entry.tier || '',
                (tags.pos || []).join(';'), tags.formality || '', tags.politeness || '', tags.transitivity || '',
                (tags.semantic || []).join(';'), (tags.style || []).join(';'), (tags.domain || []).join(';')
            ].map(v => '"' + String(v).replace(/"/g, '""') + '"').join(',');
        });
        downloadFile([headers.join(','), ...rows].join('\n'), 'tag-search-results.csv', 'text/csv');
    }

    function exportJSON() {
        if (currentResults.length === 0) { alert('No results to export.'); return; }
        downloadFile(JSON.stringify(currentResults, null, 2), 'tag-search-results.json', 'application/json');
    }

    function copyIDs() {
        if (currentResults.length === 0) { alert('No results to copy.'); return; }
        const ids = currentResults.map(e => e.id).join('\n');
        navigator.clipboard.writeText(ids).then(() => {
            alert(currentResults.length + ' entry IDs copied to clipboard.');
        }).catch(() => { alert('Failed to copy to clipboard.'); });
    }

    function downloadFile(content, filename, mimeType) {
        const blob = new Blob([content], { type: mimeType });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    }

    function switchMode(mode) {
        currentMode = mode;
        document.querySelectorAll('.mode-btn').forEach(btn => {
            btn.classList.toggle('active', btn.dataset.mode === mode);
        });
        filterPanel.style.display = mode === 'filter' ? 'block' : 'none';
        statsPanel.classList.toggle('active', mode === 'stats');
        missingPanel.classList.toggle('active', mode === 'missing');
        combinedPanel.classList.toggle('active', mode === 'combined');
        if (mode === 'stats') {
            calculateStats();
            resultsContainer.style.display = 'none';
        }
    }

    function clearFilters() {
        document.querySelectorAll('#filter-panel input[type="checkbox"]').forEach(cb => {
            cb.checked = false;
            cb.closest('label').classList.remove('checked');
        });
        document.getElementById('filter-and-mode').checked = false;
    }

    function updateCheckboxStyling(checkbox) {
        checkbox.closest('label').classList.toggle('checked', checkbox.checked);
    }

    function updateFilterCounts() {
        const entries = getAllEntries();
        if (entries.length === 0) {
            setTimeout(updateFilterCounts, 100);
            return;
        }
        const counts = { tier: new Set(), pos: new Set(), transitivity: new Set(), formality: new Set(), politeness: new Set(), semantic: new Set(), style: new Set(), domain: new Set() };
        entries.forEach(entry => {
            const tags = entry.tags || {};
            if (entry.tier) counts.tier.add(entry.tier);
            (tags.pos || []).forEach(p => counts.pos.add(p));
            if (tags.transitivity) counts.transitivity.add(tags.transitivity);
            if (tags.formality) counts.formality.add(tags.formality);
            if (tags.politeness) counts.politeness.add(tags.politeness);
            (tags.semantic || []).forEach(s => counts.semantic.add(s));
            (tags.style || []).forEach(s => counts.style.add(s));
            (tags.domain || []).forEach(d => counts.domain.add(d));
        });
        Object.entries(counts).forEach(([category, values]) => {
            const el = document.getElementById(category + '-count');
            if (el) el.textContent = '(' + values.size + ' values)';
        });
    }

    function init() {
        document.querySelectorAll('.mode-btn').forEach(btn => {
            btn.addEventListener('click', () => switchMode(btn.dataset.mode));
        });
        document.getElementById('apply-filters').addEventListener('click', applyFilters);
        document.getElementById('clear-filters').addEventListener('click', clearFilters);
        document.querySelectorAll('.filter-options input[type="checkbox"]').forEach(cb => {
            cb.addEventListener('change', () => updateCheckboxStyling(cb));
        });
        document.getElementById('find-missing').addEventListener('click', findMissingTags);
        document.getElementById('run-query').addEventListener('click', runCombinedQuery);
        document.getElementById('export-csv').addEventListener('click', exportCSV);
        document.getElementById('export-json').addEventListener('click', exportJSON);
        document.getElementById('copy-ids').addEventListener('click', copyIDs);
        paginationEl.addEventListener('click', (e) => {
            if (e.target.tagName === 'BUTTON' && e.target.dataset.page) {
                currentPage = parseInt(e.target.dataset.page, 10);
                displayResults();
                resultsContainer.scrollIntoView({ behavior: 'smooth' });
            }
        });
        updateFilterCounts();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();