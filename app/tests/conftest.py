from fastapi.testclient import TestClient
import pytest
from sqlalchemy_seed import (
    create_table,
    drop_table,
    load_fixtures,
    load_fixture_files,
)

import sys
import os

from app.services.transactions.models import Transactions

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_path, '../app'))



from app.services.db import get_db
from app.main import app


session = get_db()


# make fake data

# Transactions.insert().values({"amount":10.00, "tax":0.07, "total": 0.07, "status":"pending"})
session.query(Transactions).delete()
transaction = Transactions(amount=10.00, tax=0.17, total= 0.09, status="pending")
session.add(transaction)
session.commit()
#
# path = "/opt/service/app/tests/database_fixtures/"
# fixtures = load_fixture_files(path, ['transactions.yaml'])
# load_fixtures(session, fixtures)
