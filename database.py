from models import Cat, Breed
from typing import List

cats = [
    Cat(name="Whiskers", age=2, breed=Breed.AMERICAN_SHORTHAIR, secret_code=123456),
    Cat(name="Fluffy", age=1, breed=Breed.AMERICAN_BOBTAILED, secret_code=654321),
    Cat(name="Mittens", age=3, breed=Breed.AMERICAN_PERSIAN, secret_code=135792),
    Cat(name="Whiskerpaws", age=2, breed=Breed.AMERICAN_WELSH, secret_code=246801),
]