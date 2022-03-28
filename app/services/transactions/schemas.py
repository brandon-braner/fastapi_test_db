from pydantic import BaseModel


class TransactionsSchema(BaseModel):
    amount: float
    tax: float
    total: float
    status: str
