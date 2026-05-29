from enum import Enum
from datetime import datetime

from pydantic import BaseModel

class UnitEnum(str, Enum):
    g = "g"
    ml = "ml"
    pieces = "pieces"


class StatusEnum(str, Enum):
    good = "good"
    closetoexpiration = "closetoexpiration"
    expired = "expired"

class CreateFridgeItem(BaseModel):
    name: str
    quantity: int
    unit: UnitEnum
    status: StatusEnum
    expire_date: datetime


class UpdateFridgeItem(BaseModel):
    name: str
    quantity: int
    unit: UnitEnum
    status: StatusEnum
    expire_date: datetime