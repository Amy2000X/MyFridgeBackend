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
    ean: str
    quantity: int
    unit: UnitEnum
    status: StatusEnum
    expire_date: datetime


class UpdateFridgeItem(BaseModel):
    quantity: int
    unit: UnitEnum
    status: StatusEnum
    expire_date: datetime

class ScanBarcodeRequest(BaseModel):
    ean: str