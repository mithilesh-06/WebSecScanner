import pytest
from backend.app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_assistant_valid_question(client):
    response = client.post("/assistant/ask", json={"question": "How to test for SQL Injection?"})
    assert response.status_code == 200
    assert "answer" in response.json

def test_assistant_missing_question(client):
    response = client.post("/assistant/ask", json={})
    assert response.status_code == 400
    assert response.json["error"] == "Question required"
