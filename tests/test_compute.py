from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_compute():
    response = client.post("/api/compute", json={"x": 3, "y": 4})
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 7