from fastapi.testclient import TestClient
from .scraper import app

client = TestClient(app)

def test_response():
    response = client.post("/")
    assert response.status_code == 200