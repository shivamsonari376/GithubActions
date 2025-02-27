import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to Shivam's Flask Calculator API!" in response.data

def test_add(client):
    response = client.get('/add?a=10&b=5')
    assert response.status_code == 200
    assert response.json == {'result': 15}
