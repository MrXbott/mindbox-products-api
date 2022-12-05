from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)

def test_get_categories():
    response = client.get('/api/v1/categories/')
    assert response.status_code == 200
    assert response.json()

def test_get_category_by_id():
    category_id = 1
    category_name = 'Pasta & Macaroni'

    response = client.get(f'/api/v1/categories/{category_id}')
    assert response.status_code == 200
    assert response.json()['category_id'] == category_id
    assert response.json()['category'] == category_name
    # to do: check with products in the category

def test_get_category_by_id_not_found():
    category_id = 0
    response = client.get(f'/api/v1/categories/{category_id}')
    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}

def test_get_category_by_id_wrong_type():
    category_id = 'a'
    response = client.get(f'/api/v1/categories/{category_id}')
    assert response.status_code == 422
