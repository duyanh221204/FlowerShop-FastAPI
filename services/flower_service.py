from exceptions import raise_error
from models.flower import Flower
from schemas.flower import FlowerSchema, FlowerCreate
from sqlalchemy.orm import Session
from schemas.base_response import BaseResponse
from services.normalize_name import normalize_name


def get_all(db: Session):
    flowers = db.query(Flower).all()
    return flowers


def get_by_id(flower_id: int, db: Session) -> FlowerSchema | BaseResponse:
    if flower_id < 1:
        return raise_error(10)
    flower = db.query(Flower).filter(Flower.id == flower_id).first()
    if flower is None:
        return raise_error(200003)
    return flower


def create(flower: FlowerCreate, db: Session) -> FlowerSchema | BaseResponse:
    flower_model = db.query(Flower).filter(Flower.name == normalize_name(flower.name)).first()
    if flower_model is not None:
        return raise_error(200004)
    flower_model = Flower(
        name=normalize_name(flower.name),
        price=flower.price,
        quantity=flower.quantity,
        description=flower.description
    )
    db.add(flower_model)
    db.commit()
    return FlowerSchema(
        id=flower_model.id,
        name=flower_model.name,
        price=flower_model.price,
        quantity=flower_model.quantity,
        description=flower_model.description
    )


def update(flower_id: int, flower_update: FlowerCreate, db: Session) -> FlowerSchema | BaseResponse:
    if flower_id < 1:
        return raise_error(10)
    flower_model = db.query(Flower).filter(Flower.id == flower_id).first()
    if flower_model is None:
        return raise_error(200003)
    flower_model.name = normalize_name(flower_update.name)
    flower_model.price = flower_update.price
    flower_model.quantity = flower_update.quantity
    flower_model.description = flower_update.description
    existing_flower = db.query(Flower).filter(Flower.name == flower_model.name).first()
    if existing_flower is not None:
        return raise_error(200004)
    db.add(flower_model)
    db.commit()
    return FlowerSchema(
        id=flower_model.id,
        name=flower_model.name,
        price=flower_model.price,
        quantity=flower_model.quantity,
        description=flower_model.description
    )


def delete(flower_id: int, db: Session) -> BaseResponse:
    if flower_id < 1:
        return raise_error(10)
    flower_model = db.query(Flower).filter(Flower.id == flower_id).first()
    if flower_model is None:
        return raise_error(200003)
    db.query(Flower).filter(Flower.id == flower_id).delete()
    db.commit()
    return BaseResponse(message="Flower deleted!")