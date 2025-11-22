from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db

version = 'v1'

@asynccontextmanager
async def life_span(app: FastAPI):
    print(f"Starting the server...")
    await init_db()
    yield
    print(f"Stopping the server")


app = FastAPI(
    version=version,
    title="Bookly API",
    description="A simple REST API for book review web service - Built with Python and FastAPI",
    lifespan=life_span,
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=["books"])