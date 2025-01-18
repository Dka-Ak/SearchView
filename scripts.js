function performSearch() {
    const query = document.getElementById('search-input').value;
    if (!query) {
        alert('Please enter a search query!');
        return;
    }

    fetch('search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: query })
    })
    .then(response => response.json())
    .then(data => {
        displayResults(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function displayResults(results) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '';

    if (results.length === 0) {
        resultsDiv.textContent = 'No results found.';
    } else {
        results.forEach(result => {
            const div = document.createElement('div');
            div.textContent = result;
            resultsDiv.appendChild(div);
        });
    }
}
