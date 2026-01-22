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

    function createResultItem(entry) {
        const dirRange = entry.dirRange || '00000';
        const link = document.createElement('a');
        link.href = 'entries/' + dirRange + '/' + entry.id + '.html';
        link.className = 'result-item';

        const headwordDiv = document.createElement('div');
        headwordDiv.className = 'result-headword';
        // Note: entry.headword contains pre-escaped HTML with <ruby> tags from the build process
        headwordDiv.innerHTML = entry.headword;

        const readingDiv = document.createElement('div');
        readingDiv.className = 'result-reading';
        readingDiv.textContent = entry.reading;

        const glossDiv = document.createElement('div');
        glossDiv.className = 'result-gloss';
        glossDiv.textContent = entry.gloss;

        link.appendChild(headwordDiv);
        link.appendChild(readingDiv);
        link.appendChild(glossDiv);
        return link;
    }

    function displayResults(query, results) {
        resultsSection.style.display = 'block';

        if (results.length === 0) {
            resultsHeading.textContent = 'No results for "' + query + '"';
            resultsList.innerHTML = '';
            const noResults = document.createElement('p');
            noResults.className = 'no-results';
            noResults.textContent = 'Try a different search term.';
            resultsList.appendChild(noResults);
        } else {
            resultsHeading.textContent = results.length + ' result' + (results.length === 1 ? '' : 's') + ' for "' + query + '"';
            resultsList.innerHTML = '';
            results.forEach(function(entry) {
                resultsList.appendChild(createResultItem(entry));
            });
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