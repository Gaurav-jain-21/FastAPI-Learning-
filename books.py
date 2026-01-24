from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID

app= FastAPI()
class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description:str= Field(min_length=1, max_length=100)
    rating: int =Field(gt=-1, lt=101)

BOOKs= []

@app.get("/")
def read_api():
    return BOOKs
@app.post("/")
def create_book(book: Book):
    BOOKs.append(book)
    return book
@app.put("/update/{book_id}")
def update_book(book_id: UUID, book: Book):
    counter= 0
    for x in BOOKs:
        counter +=1
        if x.id==book_id:
            BOOKs[counter-1]=book
            return BOOKs[counter-1]
    raise HTTPException(
        status_code=404,
        detail="book id does not exist"
    )    
@app.delete("/{book_id}")
def delete_book(book_id:UUID):
    counter=0
    for x in BOOKs:
        counter +=1
        if x.id==book_id:
            del BOOKs[counter -1]
            return 'book is deleted'
    raise HTTPException(status_code=404, detail="book id not exist")    