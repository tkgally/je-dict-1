/**
 * je-dict-1 Web Application
 * A static Japanese-English learner's dictionary
 */

(function() {
    'use strict';

    // State - data is loaded from data.js (embedded at build time)
    let entriesData = null;
    let indexData = null;
    let isLoaded = false;

    // Furigana state - whether readings are visible
    let furiganaEnabled = false;

    // Pattern to match furigana notation: {kanji|reading}
    const FURIGANA_PATTERN = /\{([^|]+)\|([^}]+)\}/g;

    // DOM Elements
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

    // Kana row definitions
    const KANA_ROWS = [
        { name: 'あ行', kana: 'あいうえお' },
        { name: 'か行', kana: 'かきくけこがぎぐげご' },
        { name: 'さ行', kana: 'さしすせそざじずぜぞ' },
        { name: 'た行', kana: 'たちつてとだぢづでど' },
        { name: 'な行', kana: 'なにぬねの' },
        { name: 'は行', kana: 'はひふへほばびぶべぼぱぴぷぺぽ' },
        { name: 'ま行', kana: 'まみむめも' },
        { name: 'や行', kana: 'やゆよ' },
        { name: 'ら行', kana: 'らりるれろ' },
        { name: 'わ行', kana: 'わをん' },
    ];

    /**
     * Get the kana row for a reading based on its first character
     */
    function getKanaRow(reading) {
        if (!reading) return null;
        const firstChar = reading[0];
        for (const row of KANA_ROWS) {
            if (row.kana.includes(firstChar)) {
                return row.name;
            }
        }
        return null;
    }

    /**
     * Build the sidebar entry browser
     */
    function buildEntryBrowser() {
        if (!entriesData || !entriesData.entries) {
            entryBrowser.innerHTML = '<p class="no-entries">No entries available</p>';
            return;
        }

        // Group entries by kana row
        const grouped = {};
        for (const row of KANA_ROWS) {
            grouped[row.name] = [];
        }

        // Sort entries into groups
        const entries = Object.values(entriesData.entries);
        for (const entry of entries) {
            const rowName = getKanaRow(entry.reading);
            if (rowName && grouped[rowName]) {
                grouped[rowName].push(entry);
            }
        }

        // Sort entries within each group by reading
        for (const rowName of Object.keys(grouped)) {
            grouped[rowName].sort((a, b) => a.reading.localeCompare(b.reading, 'ja'));
        }

        // Build HTML
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

        // Add click handlers
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
        // Load furigana preference first
        loadFuriganaPreference();

        // Set up furigana toggle button
        const furiganaBtn = document.getElementById('furigana-toggle');
        if (furiganaBtn) {
            furiganaBtn.addEventListener('click', toggleFurigana);
        }

        // Load embedded data from data.js
        if (typeof DICTIONARY_DATA !== 'undefined' && typeof DICTIONARY_INDEX !== 'undefined') {
            entriesData = DICTIONARY_DATA;
            indexData = DICTIONARY_INDEX;
            isLoaded = true;

            // Update stats
            const count = entriesData.count;
            statsDiv.textContent = `${count} ${count === 1 ? 'entry' : 'entries'} available`;

            // Build the entry browser sidebar
            buildEntryBrowser();

            console.log('Dictionary loaded:', entriesData.count, 'entries');
        } else {
            console.error('Dictionary data not found. Please run the build script.');
            statsDiv.textContent = 'Error: Dictionary data not found. Please run the build script.';
        }

        // Set up event listeners
        searchForm.addEventListener('submit', handleSearch);
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
        if (!query) {
            return;
        }

        const searchType = document.querySelector('input[name="search-type"]:checked').value;
        const results = performSearch(query, searchType);

        displayResults(query, results);
    }

    /**
     * Detect the type of search query
     */
    function detectQueryType(query) {
        // Check for Japanese characters (hiragana, katakana, kanji)
        if (/[\u3040-\u309f\u30a0-\u30ff\u4e00-\u9faf]/.test(query)) {
            return 'japanese';
        }
        // Check if it's all ASCII lowercase (could be romaji or english)
        if (/^[a-z]+$/i.test(query)) {
            // Heuristic: short queries are more likely romaji
            return query.length <= 10 ? 'romaji' : 'english';
        }
        // Default to English
        return 'english';
    }

    /**
     * Perform search based on query and type
     */
    function performSearch(query, searchType) {
        const index = indexData.index;
        let entryIds = new Set();

        // Auto-detect search type if needed
        if (searchType === 'auto') {
            searchType = detectQueryType(query);
        }

        const queryLower = query.toLowerCase();

        switch (searchType) {
            case 'japanese':
                // Search Japanese index
                if (index.japanese[query]) {
                    index.japanese[query].forEach(id => entryIds.add(id));
                }
                // Also search for partial matches
                Object.keys(index.japanese).forEach(key => {
                    if (key.includes(query) && key !== query) {
                        index.japanese[key].forEach(id => entryIds.add(id));
                    }
                });
                break;

            case 'romaji':
                // Search romaji index
                if (index.romaji[queryLower]) {
                    index.romaji[queryLower].forEach(id => entryIds.add(id));
                }
                // Partial matches
                Object.keys(index.romaji).forEach(key => {
                    if (key.startsWith(queryLower) && key !== queryLower) {
                        index.romaji[key].forEach(id => entryIds.add(id));
                    }
                });
                break;

            case 'english':
                // Search English index
                const words = queryLower.split(/\s+/);
                words.forEach(word => {
                    if (index.english[word]) {
                        index.english[word].forEach(id => entryIds.add(id));
                    }
                    // Partial matches
                    Object.keys(index.english).forEach(key => {
                        if (key.startsWith(word) && key !== word) {
                            index.english[key].forEach(id => entryIds.add(id));
                        }
                    });
                });
                break;
        }

        // Convert IDs to entries
        const results = [];
        entryIds.forEach(id => {
            if (entriesData.entries[id]) {
                results.push(entriesData.entries[id]);
            }
        });

        // Sort alphabetically by reading
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

            // Add click handlers
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
     * Display a full entry
     */
    function displayEntry(entryId) {
        const entry = entriesData.entries[entryId];
        if (!entry) {
            console.error('Entry not found:', entryId);
            return;
        }

        // Store current entry ID for re-rendering on furigana toggle
        entryDisplay.dataset.currentEntryId = entryId;

        entryDisplay.innerHTML = createEntryDisplay(entry);
        entrySection.classList.remove('hidden');

        // Scroll to entry
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

        // Definitions
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

        // Examples
        if (entry.examples && entry.examples.length > 0) {
            html += `<div class="examples"><h3>Examples</h3>`;
            entry.examples.forEach(ex => {
                html += `
                    <div class="example-item">
                        <div class="example-japanese">${processJapaneseText(ex.japanese)}</div>
                        <div class="example-english">${escapeHtml(ex.english)}</div>
                        ${ex.notes ? `<div class="example-notes">${escapeHtml(ex.notes)}</div>` : ''}
                    </div>
                `;
            });
            html += `</div>`;
        }

        // Notes
        if (entry.notes) {
            html += `
                <div class="entry-notes">
                    <h3>Notes</h3>
                    <div class="notes-content">${processNotesText(entry.notes)}</div>
                </div>
            `;
        }

        // Metadata
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
     * Process Japanese text with furigana notation.
     * Converts {kanji|reading} to ruby tags when furigana is enabled,
     * or strips notation to show only kanji when disabled.
     * @param {string} text - Text that may contain furigana notation
     * @returns {string} - Safe HTML for display
     */
    function processJapaneseText(text) {
        if (!text) return '';

        // Process text: escape HTML in non-notation parts, convert notation to ruby
        const parts = [];
        let lastIndex = 0;
        let match;

        // Reset regex state
        FURIGANA_PATTERN.lastIndex = 0;

        while ((match = FURIGANA_PATTERN.exec(text)) !== null) {
            // Add escaped text before this match
            if (match.index > lastIndex) {
                parts.push(escapeHtml(text.slice(lastIndex, match.index)));
            }

            const kanji = match[1];
            const reading = match[2];

            // Add the furigana markup or plain kanji
            if (furiganaEnabled) {
                parts.push(`<ruby>${escapeHtml(kanji)}<rp>(</rp><rt>${escapeHtml(reading)}</rt><rp>)</rp></ruby>`);
            } else {
                parts.push(escapeHtml(kanji));
            }

            lastIndex = match.index + match[0].length;
        }

        // Add any remaining text
        if (lastIndex < text.length) {
            parts.push(escapeHtml(text.slice(lastIndex)));
        }

        return parts.join('');
    }

    /**
     * Process notes text with proper formatting.
     * Handles paragraphs, bullet points, and line breaks.
     * @param {string} text - Notes text that may contain formatting
     * @returns {string} - Safe HTML for display
     */
    function processNotesText(text) {
        if (!text) return '';

        // Split into paragraphs (double newline)
        const paragraphs = text.split(/\n\n+/);

        return paragraphs.map(para => {
            // Check if this paragraph contains bullet points
            const lines = para.split('\n');
            const hasBullets = lines.some(line => line.trim().startsWith('- ') || line.trim().startsWith('・'));

            if (hasBullets) {
                // Process as a list
                let html = '';
                let inList = false;
                let listItems = [];

                lines.forEach(line => {
                    const trimmed = line.trim();
                    if (trimmed.startsWith('- ') || trimmed.startsWith('・')) {
                        // Bullet point
                        const content = trimmed.replace(/^[-・]\s*/, '');
                        listItems.push(`<li>${processJapaneseText(content)}</li>`);
                        inList = true;
                    } else if (trimmed) {
                        // Regular line (could be a header before bullets)
                        if (listItems.length > 0) {
                            html += `<ul>${listItems.join('')}</ul>`;
                            listItems = [];
                        }
                        html += `<p>${processJapaneseText(trimmed)}</p>`;
                    }
                });

                // Close any remaining list
                if (listItems.length > 0) {
                    html += `<ul>${listItems.join('')}</ul>`;
                }

                return html;
            } else {
                // Regular paragraph - convert single newlines to <br>
                const processed = lines
                    .map(line => processJapaneseText(line.trim()))
                    .filter(line => line)
                    .join('<br>');
                return `<p>${processed}</p>`;
            }
        }).join('');
    }

    /**
     * Toggle furigana visibility and re-render current display
     */
    function toggleFurigana() {
        furiganaEnabled = !furiganaEnabled;

        // Update toggle button appearance
        const btn = document.getElementById('furigana-toggle');
        if (btn) {
            btn.classList.toggle('active', furiganaEnabled);
            btn.setAttribute('aria-pressed', furiganaEnabled);
        }

        // Save preference to localStorage
        try {
            localStorage.setItem('furigana-enabled', furiganaEnabled);
        } catch (e) {
            // localStorage may not be available
        }

        // Re-render sidebar
        buildEntryBrowser();

        // Re-render results if visible
        if (!resultsSection.classList.contains('hidden')) {
            const resultItems = resultsList.querySelectorAll('.result-item');
            resultItems.forEach(item => {
                const entryId = item.dataset.entryId;
                const entry = entriesData.entries[entryId];
                if (entry) {
                    item.querySelector('.headword').innerHTML = processJapaneseText(entry.headword);
                }
            });
        }

        // Re-render current entry if displayed
        if (!entrySection.classList.contains('hidden')) {
            const currentEntryId = entryDisplay.querySelector('[data-entry-id]')?.dataset.entryId ||
                                   entryDisplay.dataset.currentEntryId;
            if (currentEntryId && entriesData.entries[currentEntryId]) {
                displayEntry(currentEntryId);
            }
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
        } catch (e) {
            // localStorage may not be available
        }

        // Update button state
        const btn = document.getElementById('furigana-toggle');
        if (btn) {
            btn.classList.toggle('active', furiganaEnabled);
            btn.setAttribute('aria-pressed', furiganaEnabled);
        }
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
