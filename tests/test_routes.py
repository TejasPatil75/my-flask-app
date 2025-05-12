from app import app as flask_app


def test_home():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b'Hello, CI/CD!' in response.data
