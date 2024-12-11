
from fastapi import FastAPI ,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
import os

#initializing fastapi application
app = FastAPI()

#StaticFile is used to serve the files like css, js, images
#mount is used to map the url
app.mount('/static',StaticFiles(directory="static"),name="static")

#the jinjs2templates redner the html page dynamically
templates = Jinja2Templates(directory="templates")

#accessing env variables via os
DATABASE_URL= os.getenv("DB_URL")


#initialize db connection
dbConnnection = MongoClient(DATABASE_URL)

@app.get("/db")
async def readDb(request:Request):
    docs = dbConnnection.fastapi.learningfastapi.find({})
    for doc in docs:
        print(doc)
    return ("all good")


#here html response specify that response will be in html format
@app.get("/",response_class=HTMLResponse)
async def read_items(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.get("/message")
def return_string():
    return {"hello":"ji"}

@app.get("/items/{item_id}")
def return_itemID(item_id:int):
    return {"item_id":item_id}