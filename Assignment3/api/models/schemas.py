from pydantic import BaseModel
from typing import Optional

class SandwichBase(BaseModel):
    name: str
    description: Optional[str] = None

class SandwichCreate(SandwichBase):
    pass

class SandwichUpdate(SandwichBase):
    pass

class Sandwich(SandwichBase):
    id: int

    class Config:
        orm_mode = True
