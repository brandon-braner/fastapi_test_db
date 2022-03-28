from app.main import app
from fastapi.testclient import TestClient
client = TestClient(app)


def test_this():
    assert 1 == 1


def test_get_transactions():
    resp = client.get('/transactions')
    assert resp.json()[0]['total'] == 0.09