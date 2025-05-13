from fastapi import FastAPI
from routers import cats

app = FastAPI()

app.include_router(cats.router)
