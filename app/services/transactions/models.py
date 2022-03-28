from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from app.services.db import Base


class Transactions(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer)
    tax = Column(Integer)
    total = Column(Integer)
    status = Column(String)
    