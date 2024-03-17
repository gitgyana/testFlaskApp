from flask import Flask, request, jsonify
from link_extractor import extract_links

app = Flask(__name__)

@app.route('/api/extract-links', methods=['POST'])
def api_extract_links():
    url = request.json.get('url')
    links = extract_links(url)
    return jsonify(links)

if __name__ == '__main__':
    app.run(debug=True)
