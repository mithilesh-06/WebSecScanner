import pytest
from backend.app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_scanner_valid_url(client):
    response = client.post("/scanner/scan", json={"url": "https://example.com"})
    assert response.status_code == 200
    assert "ai_report" in response.json

def test_scanner_invalid_url(client):
    response = client.post("/scanner/scan", json={"url": ""})
    assert response.status_code == 400
    assert response.json["error"] == "URL is required"
