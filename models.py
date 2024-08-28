from pydantic import BaseModel, Field
from typing import Optional

class Item(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    name: str
    description: Optional[str] = None
    price: float

    class Config:
        allow_population_by_field_name = True
