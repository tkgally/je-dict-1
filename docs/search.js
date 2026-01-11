(function() {
    'use strict';

    const searchInput = document.getElementById('search-input');
    const searchButton = document.getElementById('search-button');
    const resultsSection = document.getElementById('results-section');
    const resultsHeading = document.getElementById('results-heading');
    const resultsList = document.getElementById('results-list');

    function detectQueryType(query) {
        if (/[\u3040-\u309f\u30a0-\u30ff\u4e00-\u9faf]/.test(query)) {
            return 'japanese';
        }
        if (/^[a-z]+$/i.test(query)) {
            return query.length <= 10 ? 'romaji' : 'english';
        }
        return 'english';
    }

    function performSearch(query, searchType) {
        if (!window.SEARCH_INDEX) return [];

        const index = window.SEARCH_INDEX;
        const entryIds = new Set();

        if (searchType === 'auto') {
            searchType = detectQueryType(query);
        }

        const queryLower = query.toLowerCase();

        if (searchType === 'japanese') {
            Object.keys(index.japanese).forEach(key => {
                if (key.includes(query)) {
                    index.japanese[key].forEach(id => entryIds.add(id));
                }
            });
        } else if (searchType === 'romaji') {
            Object.keys(index.romaji).forEach(key => {
                if (key.startsWith(queryLower)) {
                    index.romaji[key].forEach(id => entryIds.add(id));
                }
            });
        } else {
            const words = queryLower.split(/\s+/);
            words.forEach(word => {
                Object.keys(index.english).forEach(key => {
                    if (key.startsWith(word)) {
                        index.english[key].forEach(id => entryIds.add(id));
                    }
                });
            });
        }

        // Get entry data
        const results = [];
        entryIds.forEach(id => {
            if (window.SEARCH_ENTRIES && window.SEARCH_ENTRIES[id]) {
                results.push(window.SEARCH_ENTRIES[id]);
            }
        });

        return results.sort((a, b) => a.reading.localeCompare(b.reading, 'ja'));
    }

    function displayResults(query, results) {
        resultsSection.style.display = 'block';

        if (results.length === 0) {
            resultsHeading.textContent = 'No results for "' + query + '"';
            resultsList.innerHTML = '<p class="no-results">Try a different search term.</p>';
        } else {
            resultsHeading.textContent = results.length + ' result' + (results.length === 1 ? '' : 's') + ' for "' + query + '"';
            resultsList.innerHTML = results.map(function(entry) {
                const folder = entry.folder || 'a';
                const prefix = entry.prefix || entry.id.substring(0, 2);
                return '<a href="entries/' + folder + '/' + prefix + '/' + entry.id + '.html" class="result-item">' +
                    '<div class="result-headword">' + entry.headword + '</div>' +
                    '<div class="result-reading">' + entry.reading + '</div>' +
                    '<div class="result-gloss">' + entry.gloss + '</div>' +
                '</a>';
            }).join('');
        }
    }

    function handleSearch() {
        const query = searchInput.value.trim();
        if (!query) return;

        const searchType = document.querySelector('input[name="search-type"]:checked').value;
        const results = performSearch(query, searchType);
        displayResults(query, results);
    }

    searchButton.addEventListener('click', handleSearch);
    searchInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') handleSearch();
    });
})();