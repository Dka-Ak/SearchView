from flask import Flask, request, jsonify, session
from googlesearch import search
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

@app.route('/search', methods=['POST'])
def perform_search():
    data = request.get_json()
    query = data.get('query', '')

    if query:
        session['search_query'] = query
        results = search(query, num_results=10)  # Number of results can be adjusted

        # End the session after search
        session.clear()

        return jsonify(results)
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)
