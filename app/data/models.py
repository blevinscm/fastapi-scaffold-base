import typing
from odmantic import Model
from pydantic import BaseModel


#MongodDB - uncomment to use odmantic and MongoDB
class Hug(Model):
    kind: str
    hug_size: float
    hugger: str

# POSTGRES - uncomment to use Pydantic and PG
# class Hug(BaseModel):
#     hug: str
#     hug_size: float
#     hugger: str
