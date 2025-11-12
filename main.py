from books_data import books
from fastapi import FastAPI
from schemas import Book
from typing import List


app = FastAPI()

@app.get('/books', response_model=List[Book])
async def get_all_books() -> dict:
    return books

@app.post('/books')
async def update_book() -> dict:
    pass

@app.get('/book/{book_id}')
async def get_book_by_id(book_id: int) -> dict:
    pass

@app.patch('/book/{book_id}')
async def update_book(book_id: int) -> dict:
    pass

@app.delete('/book/{book_id}')
async def delete_book(book_id: int) -> dict:
    pass



