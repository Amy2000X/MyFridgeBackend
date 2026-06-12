from enum import Enum
from datetime import datetime

from pydantic import BaseModel

class Product(BaseModel):
    id: int
    ean: str
    name: str | None
    brand: str | None

    quantity: float | None
    unit: str | None

    energy_kcal_100g: float | None
    protein_100g: float | None
    carbs_100g: float | None
    fat_100g: float | None