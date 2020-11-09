from typing import List

from fastapi import FastAPI, HTTPException

from odmantic import AIOEngine, Model, ObjectId


class Hug(Model):
    kind: str
    hug_size: float
    hugger: str


engine = AIOEngine()


@app.put("/hugs/", response_model=Hug)
async def new_hug(hug: Hug):
    await engine.save(hug)
    return hug


@app.get("/hugs/", response_model=List[Hug])
async def get_hugs():
    trees = await engine.find(Hug)
    return trees


@app.get("/hugs/count", response_model=int)
async def count_hugs():
    count = await engine.count(Hug)
    return count


@app.get("/hugs/{id}", response_model=Hug)
async def get_tree_by_id(id: ObjectId):
    hug = await engine.find_one(Hug, Hug.id == id)
    if hug is None:
        raise HTTPException(404)
    return hug
