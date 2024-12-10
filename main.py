from typing import Union
from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def return_string():
    return {"hello":"ji"}

@app.get("/items/{item_id}")
def return_itemID(item_id:int):
    return {"item_id":item_id}