from fastapi import FastAPI
from app.services.transactions.routes import router as transactions_router
from app.services.transactions.models import Base
from app.services.db import engine
app = FastAPI()

app.include_router(transactions_router)

Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}
