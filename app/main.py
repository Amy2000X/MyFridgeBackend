from fastapi import FastAPI
from .schemas import User

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/register")
def register_user():
    test = User(email="test@gmail.com", password="Testing123!")
    print(test.email)
    return {"email:": test.email, "test_password": test.password}