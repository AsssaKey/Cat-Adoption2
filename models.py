from pydantic import BaseModel, Field  
from enum import Enum

class Breed(Enum):
    AMERICAN_SHORTHAIR = "american_shorthair"
    AMERICAN_BOBTAILED = "american_bobtailed"
    AMERICAN_PERSIAN = "american_persian"
    AMERICAN_WELSH = "american_welsh"
    
class Cat(BaseModel):
    name: str = Field(min_length=2, max_length=15)
    age: int = Field(gt=0, lt=30)
    breed: Breed
    secret_code: int

class CatOut(BaseModel):
    name: str
    age: int
    breed: Breed
    