from app import create_app
import os


def test_home_page(test_client):
    response = test_client.get('/')
    assert response.status_code == 200

def test_login_page(test_client):
    response = test_client.get('/login')
    assert response.status_code == 200

def test_register_page(test_client):
    response = test_client.get('/register')
    assert response.status_code == 200

def test_random_page(test_client):
    response = test_client.get('/nothing')
    assert response.status_code == 404
