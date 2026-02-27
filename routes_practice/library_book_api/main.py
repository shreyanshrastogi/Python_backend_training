from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# from typing import Any
app: FastAPI = FastAPI()


class Book(BaseModel):
    title: str
    author: str
    copies_available: int


library: dict[int, Book] = {}


# list all books
@app.get("/books")
def all_books() -> dict[int, Book]:
    return library


# get one book detail
@app.get("/book/{book_id}")
def book_detail(book_id: int) -> Book:
    if book_id not in library:
        raise HTTPException(status_code=404, detail="Book not found")
    return library[book_id]


# add a books
@app.post("/books/add/{book_id}")
def add_book(book_id: int, book_data: Book) -> dict[str, str | Book]:
    if book_id in library:
        raise HTTPException(status_code=409, detail="book already present")

    library[book_id] = book_data
    return {"message": "book added successfully", "book_data": book_data}


# remove a book
@app.delete("/books/remove/{book_id}")
def remove_book(book_id: int) -> dict[str, str]:
    if book_id not in library:
        raise HTTPException(status_code=404, detail="book not found")

    del library[book_id]
    return {"message": f" {book_id} removed successfully"}


# issue a book
@app.put("/books/issue/{book_id}")
def issue_book(book_id: int) -> dict[str, object]:

    if book_id not in library:
        raise HTTPException(status_code=404, detail="book not found")
    if library[book_id].copies_available == 0:
        raise HTTPException(status_code=400, detail="book not available")

    library[book_id].copies_available -= 1
    return {
        "message": "book issued",
        "book": {"title": library[book_id].title, "author": library[book_id].author},
    }


# return book
@app.put("/books/return/{book_id}")
def return_book(book_id: int) -> dict[str, str | Book]:
    if book_id not in library:
        raise HTTPException(status_code=404, detail="book not from our library")
    library[book_id].copies_available += 1
    return {"message": "book returned successfully", "book_detail": library[book_id]}
