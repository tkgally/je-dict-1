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
                const dirRange = entry.dirRange || '00000';
                return '<a href="entries/' + dirRange + '/' + entry.id + '.html" class="result-item">' +
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

    // Also handle header search input if it exists on this page
    const headerSearchInput = document.getElementById('header-search-input');
    const headerSearchButton = document.getElementById('header-search-button');

    if (headerSearchInput && headerSearchButton) {
        function handleHeaderSearch() {
            const query = headerSearchInput.value.trim();
            if (!query) return;

            // Copy query to main search input for consistency
            searchInput.value = query;

            // Use auto-detect for header search
            const searchType = detectQueryType(query);
            const results = performSearch(query, searchType);
            displayResults(query, results);

            // Clear header search input after search
            headerSearchInput.value = '';

            // Scroll to results
            if (resultsSection) {
                resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }

        headerSearchButton.addEventListener('click', handleHeaderSearch);
        headerSearchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') handleHeaderSearch();
        });
    }

    // Check for URL parameters (from header search)
    function handleUrlParams() {
        const params = new URLSearchParams(window.location.search);
        const query = params.get('q');
        const searchType = params.get('type') || 'auto';

        if (query) {
            // Set the search input value
            searchInput.value = query;

            // Set the radio button if specified
            if (searchType && searchType !== 'auto') {
                const radio = document.querySelector('input[name="search-type"][value="' + searchType + '"]');
                if (radio) radio.checked = true;
            }

            // Perform the search
            const results = performSearch(query, searchType);
            displayResults(query, results);

            // Clean up URL (remove query params)
            if (window.history.replaceState) {
                window.history.replaceState({}, document.title, window.location.pathname);
            }
        }
    }

    // Run URL param check after search index is loaded
    if (window.SEARCH_INDEX) {
        handleUrlParams();
    } else {
        // Wait for search index to load, then check params
        var checkInterval = setInterval(function() {
            if (window.SEARCH_INDEX) {
                clearInterval(checkInterval);
                handleUrlParams();
            }
        }, 50);
        // Stop checking after 5 seconds
        setTimeout(function() { clearInterval(checkInterval); }, 5000);
    }
})();