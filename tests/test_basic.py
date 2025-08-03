import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from app.main import app, url_store


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_shorten_url(client):
    response = client.post('/api/shorten', json={'url': 'https://www.example.com'})
    assert response.status_code == 201
    data = response.get_json()
    assert 'short_code' in data
    assert data['short_url'].startswith('http://localhost:5000/')

def test_redirect_and_stats(client):
    resp = client.post('/api/shorten', json={'url': 'https://example.com'})
    code = resp.get_json()['short_code']

    redir = client.get(f'/{code}')
    assert redir.status_code == 302

    stats = client.get(f'/api/stats/{code}')
    assert stats.status_code == 200
    data = stats.get_json()
    assert data['clicks'] == 1
    assert data['url'] == 'https://example.com'

def test_invalid_url(client):
    resp = client.post('/api/shorten', json={'url': 'bad_url'})
    assert resp.status_code == 400

def test_missing_url(client):
    resp = client.post('/api/shorten', json={})
    assert resp.status_code == 400

def test_nonexistent_stats(client):
    resp = client.get('/api/stats/notreal')
    assert resp.status_code == 404
