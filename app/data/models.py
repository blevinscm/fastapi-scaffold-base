import typing
from odmantic import Model


class Hug(Model):
    kind: str
    hug_size: float
    hugger: str