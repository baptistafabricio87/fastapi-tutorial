from typing import Optional

from fastapi import FastAPI


app = FastAPI(title="Tutorial")


@app.get("/")
def hello():
    return {"msg": "Hello World!"}


@app.get("/item/{item}")
def read_item(item_id: int, name: Optional[str] = None):
    return {"item_id": item_id, "name": name}
