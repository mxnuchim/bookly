from fastapi import FastAPI, Header
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def read_root():
    return {"message": "Server s live and running"}

@app.get('/greet')
# Each path parameter in the handler function will be expected as a query as long as you do not define it in the url
# In this case, name will be passed as a query and validation is handled by pydantic -> FastAPI relies on pydantic for input validation
async def greet_user(name: Optional[str] = "User", age: int = 0) -> dict:
    return {"message": f"Howdy {name}!, You are {age} years old", "server_status": f"100%! The server is live and running 🚀🚀"}

class CreateBookModel(BaseModel):
    title: str
    author: str
    favorite: bool = False

@app.post('/create_book')
async def create_book(book_data: CreateBookModel) -> dict:
    print(f"Book data received --->> {book_data.model_dump()}")
    return {
        "title": book_data.title,
        "author": book_data.author,
        "favorite": book_data.favorite
    }

@app.get("/get_headers", status_code=200) # you can specify the status code to return. status_code is optional, but it's a good practice to set it
async def get_headers(
    accept: str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
    host: str = Header(None)
):
    request_headers: dict = {}
    
    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type
    request_headers["User-Agent"] = user_agent
    request_headers["Host"] = host

    return {"headers": request_headers}