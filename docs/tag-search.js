/**
 * Tag-Based Search functionality for je-dict-1 dictionary
 * Simplified version: Filter by tier, POS, and formality
 */
(function() {
    'use strict';

    const RESULTS_PER_PAGE = 50;

    let currentResults = [];
    let currentPage = 1;
    let currentMode = 'filter';

    const filterPanel = document.getElementById('filter-panel');
    const statsPanel = document.getElementById('stats-panel');
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

    function getSelectedFilters() {
        const filters = {};
        const categories = ['tier', 'pos', 'formality'];
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

    function displayResults() {
        resultsContainer.style.display = 'block';
        const total = currentResults.length;
        const totalPages = Math.ceil(total / RESULTS_PER_PAGE);
        const start = (currentPage - 1) * RESULTS_PER_PAGE;
        const end = Math.min(start + RESULTS_PER_PAGE, total);
        const pageResults = currentResults.slice(start, end);

        resultsCountEl.textContent = total + ' entries found (showing ' + (start + 1) + '-' + end + ')';

        resultsListEl.innerHTML = pageResults.map(entry => {
            const tags = entry.tags || {};
            const posStr = (tags.pos || []).join(', ');
            const tagSummary = [posStr, tags.formality].filter(Boolean).join(' | ');
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
        const stats = { total: entries.length, tier: {}, pos: {}, formality: {} };

        entries.forEach(entry => {
            const tags = entry.tags || {};
            // Tier
            const tier = entry.tier || 'unknown';
            stats.tier[tier] = (stats.tier[tier] || 0) + 1;
            // POS
            const pos = tags.pos || [];
            pos.forEach(p => { stats.pos[p] = (stats.pos[p] || 0) + 1; });
            // Formality
            const formality = tags.formality || '(missing)';
            stats.formality[formality] = (stats.formality[formality] || 0) + 1;
        });

        const statsGrid = document.getElementById('stats-grid');
        statsGrid.innerHTML =
            '<div class="stats-card"><h3>Overview</h3>' +
            '<div class="stats-item"><span>Total entries</span><span class="stats-value">' + stats.total + '</span></div></div>' +
            '<div class="stats-card"><h3>Vocabulary Tier</h3>' + renderStatsItems(stats.tier, stats.total) + '</div>' +
            '<div class="stats-card"><h3>Part of Speech</h3>' + renderStatsItems(stats.pos, stats.total) + '</div>' +
            '<div class="stats-card"><h3>Formality</h3>' + renderStatsItems(stats.formality, stats.total) + '</div>';
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
        const headers = ['id', 'headword', 'reading', 'gloss', 'tier', 'pos', 'formality'];
        const rows = currentResults.map(entry => {
            const tags = entry.tags || {};
            return [entry.id, entry.headword.replace(/<[^>]+>/g, ''), entry.reading, entry.gloss, entry.tier || '',
                (tags.pos || []).join(';'), tags.formality || ''
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

    function init() {
        document.querySelectorAll('.mode-btn').forEach(btn => {
            btn.addEventListener('click', () => switchMode(btn.dataset.mode));
        });
        document.getElementById('apply-filters').addEventListener('click', applyFilters);
        document.getElementById('clear-filters').addEventListener('click', clearFilters);
        document.querySelectorAll('.filter-options input[type="checkbox"]').forEach(cb => {
            cb.addEventListener('change', () => updateCheckboxStyling(cb));
        });
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
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
