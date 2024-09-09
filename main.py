from fastapi import FastAPI
from configs.database import Base, engine
from models import *

app = FastAPI()

Base.metadata.create_all(bind=engine)