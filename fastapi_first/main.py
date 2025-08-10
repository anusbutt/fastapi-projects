from fastapi import FastAPI, Path
from typing import Optional 
from pydantic import BaseModel


app = FastAPI()

items = {
    1: {
        "name": "Majestic",
        "item_type": "Women",
        "price": 2500
    }
}

class Items(BaseModel):
    name: str
    item_type: str
    price: int

class UpdateItem(BaseModel):
    name: Optional[str] = None
    item_type: Optional[str] = None
    price: Optional[int] = None

@app.get("/")
def home():
    return{"Hello!"}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(..., description="enter id to view details", gt=0)):
    return items[item_id]

@app.get("/get-by-name/{item_id}")
def get_by_name(item_id: int,name: Optional[str] = None):
    for item_id in items:
        if items[item_id]["name"] == name:
            return items[item_id]
    return {"data": "not found"}

@app.post("/add-item/{item_id}")
def add_item(item_id: int, item: Items):
    if item_id in items:
        return {"error": "already exists"}
    items[item_id] = item.dict()
    return items[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in items:
        return {"error": "item not found"}
    
    if item.name != None:
        items[item_id].name = item.name

    if item.item_type != None:
        items[item_id].item_type = item.item_type

    if item.price != None:
        items[item_id].price = item.price
    return items[item_id]

@app.delete("/delete-item/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        return {"error": "item not found"}
    del items[item_id]
    return {"message": "item deleted succesfully"}