from pydantic import BaseModel


class Transactions(BaseModel):
    amount: float
    tax: float
    total: float
    status: str
