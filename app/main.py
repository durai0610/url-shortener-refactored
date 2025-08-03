from flask import Flask, request, jsonify, redirect, abort
from datetime import datetime, UTC
from app.utils import generate_short_code, is_valid_url
from app.models import url_store
import threading

app = Flask(__name__)
lock = threading.Lock()

@app.route('/')
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "URL Shortener API"
    })

@app.route('/api/health')
def api_health():
    return jsonify({
        "status": "ok",
        "message": "URL Shortener API is running"
    })

@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({'error': 'Missing URL'}), 400

    long_url = data['url']
    if not is_valid_url(long_url):
        return jsonify({'error': 'Invalid URL'}), 400

    short_code = generate_short_code()
    with lock:
        while short_code in url_store:
            short_code = generate_short_code()
        url_store[short_code] = {
            'url': long_url,
            'created_at': datetime.now(UTC).isoformat(),
            'clicks': 0
        }

    return jsonify({
        'short_code': short_code,
        'short_url': f'http://localhost:5000/{short_code}'
    }), 201

@app.route('/<short_code>', methods=['GET'])
def redirect_to_url(short_code):
    with lock:
        entry = url_store.get(short_code)
        if not entry:
            return abort(404)
        entry['clicks'] += 1
        return redirect(entry['url'])

@app.route('/api/stats/<short_code>', methods=['GET'])
def get_stats(short_code):
    entry = url_store.get(short_code)
    if not entry:
        return jsonify({'error': 'Short code not found'}), 404

    return jsonify({
        'url': entry['url'],
        'clicks': entry['clicks'],
        'created_at': entry['created_at']
    })
