from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.services.db import get_db
from app.services.transactions.models import Transactions
from app.services.transactions.schemas import TransactionsSchema

router = APIRouter(prefix="/transactions")


@router.get("/")
async def transactions(db: Session = Depends(get_db)):
    transactions = db.query(Transactions).all()
    return transactions
