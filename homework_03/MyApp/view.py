from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def home_page():
    return {"message": "Hello!"}


@router.get("/ping/")
def ping_page():
    return {"message": "pong"}