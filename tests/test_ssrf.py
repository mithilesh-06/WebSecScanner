import pytest
from backend.app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_ssrf_valid_test(client):
    response = client.post("/ssrf/test", json={"url": "https://example.com", "payload": "http://localhost"})
    assert response.status_code == 200
    assert "ai_report" in response.json

def test_ssrf_missing_url(client):
    response = client.post("/ssrf/test", json={"payload": "http://localhost"})
    assert response.status_code == 400
    assert response.json["error"] == "Target URL required"
