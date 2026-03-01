import pytest
from app import create_app, db

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
    })

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()


def test_create_user(client):
    response = client.post('/users', json={
        "name": "Kauan", 
        "email": "kauan@email.com"
    })
    assert response.status_code == 201
    assert response.json['message'] == "User created successfully!"

def test_create_user_with_bad_email(client):
    response = client.post('/users', json={
        "name": "Kauan",
        "email": "isto-nao-e-um-email"
    })
    assert response.status_code == 400
    assert "Invalid e-mail format" in response.json['error']

def test_list_users_empty(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert response.json['message'] == "No users found in the database."
    assert response.json['users'] == []

def test_list_users_with_data(client):
    client.post('/users', json={
        "name": "Kauan", 
        "email": "kauan@email.com"
    })
    response = client.get('/users')
    assert response.status_code == 200
    assert "Successfully retrieved" in response.json['message']
    assert len(response.json['users']) == 1

def test_get_single_user(client):
    client.post('/users', json={
        "name": "Kauan", 
        "email": "kauan@email.com"
    })
    response = client.get('/users/1')
    assert response.status_code == 200
    assert response.json['message'] == "User with ID 1 found successfully."
    assert response.json['user']['name'] == "Kauan"

def test_get_user_not_found(client):
    response = client.get('/users/99')
    assert response.status_code == 404
    assert "does not exist in our records" in response.json['message']

def test_update_user(client):
    client.post('/users', json={
        "name": "Kauan", 
        "email": "kauan@email.com"
    })
    response = client.put('/users/1', json={"name": "Kauan Amarante"})
    assert response.status_code == 200
    assert response.json['message'] == "User 1 updated successfully!"

def test_delete_user(client):
    client.post('/users', json={
        "name": "Kauan", 
        "email": "kauan@email.com"
    })
    response = client.delete('/users/1')
    assert response.status_code == 200
    assert "successfully deleted" in response.json['message']