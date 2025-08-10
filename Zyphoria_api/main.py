from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel
from typing import Optional, Dict
from enum import Enum

app = FastAPI()

# --- Enum for Fragrance Types ---
class FragranceType(str, Enum):
    men = "men"
    women = "women"
    unisex = "unisex"

# --- Pydantic Models ---
class Fragrance(BaseModel):
    name: str
    brand: str
    fragrance_type: FragranceType
    price: float
    description: Optional[str] = None

class UpdateFragrance(BaseModel):
    name: Optional[str]
    brand: Optional[str]
    fragrance_type: Optional[FragranceType]
    price: Optional[float]
    description: Optional[str]

# --- In-Memory "Database" ---
fragrances: Dict[int, Fragrance] = {
    1: Fragrance(name="Aqua Essence", brand="Hugo Boss", fragrance_type=FragranceType.men, price=49.99),
    2: Fragrance(name="Oceanic Rush", brand="Dior", fragrance_type=FragranceType.men, price=59.99),
    3: Fragrance(name="Urban Night", brand="Gucci", fragrance_type=FragranceType.men, price=55.50),
    4: Fragrance(name="Bold Flame", brand="Armani", fragrance_type=FragranceType.men, price=62.00),
    5: Fragrance(name="Floral Dream", brand="Chanel", fragrance_type=FragranceType.women, price=70.00),
    6: Fragrance(name="Soft Breeze", brand="YSL", fragrance_type=FragranceType.women, price=65.99),
    7: Fragrance(name="Rose Charm", brand="Versace", fragrance_type=FragranceType.women, price=80.00),
    8: Fragrance(name="Velvet Touch", brand="Givenchy", fragrance_type=FragranceType.women, price=72.50),
    9: Fragrance(name="Neutral Soul", brand="CK", fragrance_type=FragranceType.unisex, price=50.00),
    10: Fragrance(name="Musk Harmony", brand="Tom Ford", fragrance_type=FragranceType.unisex, price=85.00),
}


@app.get("/")
def home():
    return {"message": "fragrance API is running"}


@app.get("/fragrances")
def get_all_fragrances(fragrance_type: Optional[FragranceType] = Query(None, description="search by filter")):
    if fragrance_type:
        return {fid: f for fid, f in fragrances.items() if f.fragrance_type == fragrance_type}
    return fragrances


@app.get("/fragrances/{fragrance_id}")
def get_fragrance(fragrance_id: int = Path(..., gt=0 , description = "search by id")):
    if fragrance_id not in fragrances:
        raise HTTPException(status_code=400, detail="fragrance not found")
    return fragrances[fragrance_id]


@app.get("/search")
def search_by_name(name: str):
    results = [f for f in fragrances.values() if f.name.lower() == name.lower()]
    return results or {"message": "no matching fragrance found"}

@app.post("/fragrances/{fragrance_id}")
def add_fragrance(fragrance_id: int, fragrance: Fragrance):
    if fragrance_id in fragrances:
        raise HTTPException(status_code=400, detail="fragrance id already exist")
    fragrances[fragrance_id] = fragrance
    return {"message": "fragrance succesfully added", "data": fragrance}

@app.put("/fragrances/{fragrance_id}")
def update_fragrance(fragrance_id: int, updated: UpdateFragrance):
    if fragrance_id not in fragrances:
        raise HTTPException(status_code=400, detail="fragrance not found")
    stored = fragrances[fragrance_id]
    updated_data = updated.dict(exclude_unset=True)
    updated_fragrance = stored.copy(update=updated_data)
    fragrances[fragrance_id] = updated_fragrance
    return {"message": "fragrance updated", "data": updated_fragrance}

@app.delete("/fragrances/{fragrance_id}")
def delete_fragrance(fragrance_id: int):
    if fragrance_id not in fragrances:
        raise HTTPException(status_code=400, detail="fragrance not found")
    del fragrances[fragrance_id]
    return {"message": f"fragrance {fragrance_id} succesfully deleted"}
