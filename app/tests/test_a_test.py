from unittest import mock

from app.main import app
from fastapi.testclient import TestClient

from app.services.db import get_db

client = TestClient(app)


def test_get_transaction_mock():
    get_db_mock = mock.MagicMock(spec=get_db)
    db = mock.MagicMock()
    query = mock.MagicMock()
    all = mock.MagicMock()
    get_db_mock.db.return_value.query.return_value.all.return_value = [{
        'id': 1,
        'amount': 10.70,
        'description': 'test',
        'tax':1.00,
        'total': 11.70
    }]
    app.dependency_overrides[get_db] = lambda: get_db_mock

    resp = client.get('/transactions')
    assert resp.json()[0]['amount'] == 10.70

def test_get_transactions():
    resp = client.get('/transactions')
    print(resp.json())
    assert resp.json()[0]['amount'] == 10.70