from fastapi import FastAPI
from configs.database import Base, engine
from models import *
from routers import auth, user, flower, customer, seller

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(flower.router)
app.include_router(customer.router)
app.include_router(seller.router)
app.include_router(user.router)