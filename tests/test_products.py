import pytest


@pytest.mark.anyio
async def test_get_products(async_client):
    response = await async_client.get('/products/')
    assert response.status_code == 200

@pytest.mark.anyio
async def test_get_product_by_id(async_client):
    product_id = 1
    response = await async_client.get(f'/products/{product_id}')
    assert response.status_code == 200
    assert response.json() == {
        "product_id":1,
        "product_name":"Onion",
        "brand":"Fresho",
        "categories":[{"category_id":53,"category":"Vegetables"}]}

# client = TestClient(app)

# def test_get_products(client):
#     response = client.get('/api/v1/products/')
#     assert response.status_code == 200
#     assert response.json()

# def test_get_product_by_id(client):
#     product_id = 1
#     response = client.get(f'/api/v1/products/{product_id}')
#     assert response.status_code == 200
#     assert response.json() == {
#         "product_id":1,
#         "product_name":"Onion",
#         "brand":"Fresho",
#         "categories":[{"category_id":53,"category":"Vegetables"}]}

def test_get_product_by_id_not_found(client):
    product_id = 0
    response = client.get(f'/api/v1/products/{product_id}')
    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}

def test_get_product_by_id_wrong_type(client):
    product_id = 'a'
    response = client.get(f'/api/v1/products/{product_id}')
    assert response.status_code == 422
    
    