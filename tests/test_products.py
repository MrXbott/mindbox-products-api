import pytest


@pytest.mark.anyio
async def test_get_products(async_client):
    response = await async_client.get('/products/')
    assert response.status_code == 200
    assert response.json()

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

@pytest.mark.anyio
async def test_get_product_by_id_not_found(async_client):
    product_id = 0
    response = await async_client.get(f'/products/{product_id}')
    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}

@pytest.mark.anyio
async def test_get_product_by_id_wrong_type(async_client):
    product_id = 'a'
    response = await async_client.get(f'/products/{product_id}')
    assert response.status_code == 422

# to do: should I test rate limits? how?