from app import create_app
import os


def test_home_page():
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200

def test_login_page():
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.get('/login')
        assert response.status_code == 200

def test_register_page():
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    with flask_app.test_client() as test_client:
        response = test_client.get('/register')
        assert response.status_code == 200
