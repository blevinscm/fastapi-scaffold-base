import typing
from odmantic import AIOEngine, Model, ObjectId


class Hug(Model):
    kind: str
    hug_size: float
    hugger: str