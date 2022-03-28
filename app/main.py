from fastapi import FastAPI
from app.services.transactions.routes import router as transactions_router

app = FastAPI()

app.include_router(transactions_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
