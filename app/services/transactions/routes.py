from fastapi import APIRouter

router = APIRouter(prefix="/transactions")


@router.get("/")
def transactions():
    return {"message": "Hello transactions"}
