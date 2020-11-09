from fastapi import APIRouter
from data import models

router = APIRouter()


@router.get("/hugs/", tags=["Friendly_Hugs"])
async def read_hugs():
    """
    Returns all huggers available
    """
    return [{"hugs": "Pooh"}, {"username": "Bear"}]


@router.get("/hugs/me", tags=["Friendly_Hugs"])
async def read_huggee_me():
    """
    Set to return user context. In this case the hugee.
    """
    return {"username": "Huggable Developer"}


@router.get("/hugs/{type}", tags=["Friendly_Hugs"])
async def read_hug_type(hug_type: str):
    """
    Allows user to enter the type of hug they want.
    Replace with any single non-enum type.
    """
    return {"username": hug_type}
