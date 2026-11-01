import uvicorn
from fastapi import FastAPI, status
from pydantic import BaseModel


app = FastAPI()


book: list[Book] = []


class Book(BaseModel):
    book: str


@app.get("/books", status_code=status.HTTP_200_OK)
def read_books():
    return book


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(payload: Book):
    new_book = Book(book=payload.book)
    book.append(new_book)
    return new_book


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
