from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional, Dict

app = FastAPI(title="Book Review API")

class Book(BaseModel):
    title: str = Field(..., example="The Pragmatic Programmer")
    author: str = Field(..., example="Andy Hunt")
    genre: str = Field(..., example="Programming")
    description: Optional[str] = Field(None, example="A great book about software craftsmanship.")

class Review(BaseModel):
    reviewer: str
    rating: int = Field(..., gt=0, le=5)
    comment: Optional[str] = None

class BookOut(Book):
    id: int

class ReviewOut(BaseModel):
    book_id: int
    reviews: List[Review]

books: Dict[int, Book] = {}
reviews: Dict[int, List[Review]] = {}
book_id_counter = 1

@app.post("/books", response_model=BookOut)
def add_book(book: Book):
    global book_id_counter
    books[book_id_counter] = book
    current_id = book_id_counter
    book_id_counter += 1
    return BookOut(id=current_id, **book.dict())


@app.get("/books", response_model=List[BookOut])
def list_books():
    return [BookOut(id=book_id, **book.dict()) for book_id, book in books.items()]


@app.get("/book/{book_id}", response_model=BookOut)
def get_book(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    return BookOut(id=book_id, **books[book_id].dict())


@app.post("/book/{book_id}/reviews", response_model=ReviewOut)
def add_review(book_id: int, review: Review):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    reviews.setdefault(book_id, []).append(review)
    return ReviewOut(book_id=book_id, reviews=reviews[book_id])


@app.get("/book/{book_id}/reviews", response_model=ReviewOut)
def get_review(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    return ReviewOut(book_id=book_id, reviews=reviews.get(book_id, []))
