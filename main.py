from fastapi import FastAPI
from configs.database import Base, engine
from models import *
from routers import auth

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)