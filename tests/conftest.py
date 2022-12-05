import pytest
from fastapi.testclient import TestClient

from httpx import AsyncClient

from app.main import app


@pytest.fixture(scope='module')
def client():
    client = TestClient(app)
    yield client  # testing happens here


@pytest.fixture()
async def async_client():
    async with AsyncClient(
            app=app,
            base_url='http://localhost:8000/api/v1',
            headers={'Content-Type': 'application/json'}
    ) as client:
        yield client
