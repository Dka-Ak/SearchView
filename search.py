from flask import Flask, request, jsonify
from googlesearch import search

app = Flask(__name__)

@app.route('/search', methods=['POST'])
def perform_search():
    data = request.get_json()
    query = data.get('query', '')

    if query:
        results = search(query, num_results=10)  # Number of results can be adjusted
        return jsonify(results)
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)
