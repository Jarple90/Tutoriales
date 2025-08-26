from fastapi.testclient import TestClient
from backend_frontend.main import app

client = TestClient(app)

def test_list_items():
    response = client.get("/stock/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
