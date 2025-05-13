from fastapi import APIRouter, HTTPException, Response
from database import cats
from models import Cat, CatOut

router = APIRouter()

@router.get("/cats", response_model=list[CatOut])
async def get_cats():
    return cats

@router.post("/cats")
async def create_cat(cat: Cat):
    for existing_cat in cats:
        if existing_cat.name == cat.name:
            raise HTTPException(status_code=400, detail="Cat already exists")
    cats.append(cat)
    return {"message": "Cat added successfully"}    

@router.delete("/cats/{cat_name}")
async def delete_cat(cat_name: str):
    for cat in cats:
        if cat.name == cat_name:
            cats.remove(cat)
            return {"message": "Cat deleted successfully"}
    raise HTTPException(status_code=404, detail="Cat not found")

@router.get("/stats/cats")
async def count_cats():
    total = len(cats)
    kittens = 0
    adults = 0
    seniors = 0
    for cat in cats:
        if cat.age < 1:
            kittens += 1
        elif cat.age < 3:
            adults += 1
        else:
            seniors += 1
    return{
        "total": total,
        "kittens": kittens,
        "adults": adults,
        "seniors": seniors
    }
    