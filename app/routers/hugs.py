from fastapi import APIRouter, HTTPException
from app.data import models
from typing import List
from odmantic import AIOEngine, ObjectId

router = APIRouter()

Hug = models.Hug
engine = AIOEngine()

@router.put("/hugs/", response_model=Hug, tags=["hugs"])
async def new_hug(hug: Hug):
    await engine.save(hug)
    return hug


@router.get("/hugs/", response_model=List[Hug], tags=["hugs"])
async def get_hugs():
    trees = await engine.find(Hug)
    return trees


@router.get("/hugs/count", response_model=int, tags=["hugs"])
async def count_hugs():
    count = await engine.count(Hug)
    return count


@router.get("/hugs/{id}", response_model=Hug, tags=["hugs"])
async def get_hug_by_id(id: ObjectId):
    hug = await engine.find_one(Hug, Hug.id == id)
    if hug is None:
        raise HTTPException(404)
    return hug