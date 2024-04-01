from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index_page():
    return {"message": "Hello"}


@app.get("/ping/")
def ping_page():
    return {"message": "pong"}