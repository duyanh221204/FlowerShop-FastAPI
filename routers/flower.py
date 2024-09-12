from fastapi import APIRouter, Depends
from exceptions import raise_error
from schemas.flower import FlowerCreate
from configs.database import get_db
from configs.authentication import get_current_user
from services.flower_service import get_all, get_by_id, create, update, delete

router = APIRouter(
    prefix="/api/flower",
    tags=["Flower"]
)


@router.get("/get-flowers")
async def get_flowers(db=Depends(get_db)):
    try:
        return get_all(db)
    except Exception:
        return raise_error(200001)


@router.get("/get-flower-by-id/{flower_id}")
async def get_flower_by_id(flower_id: int, db=Depends(get_db)):
    try:
        return get_by_id(flower_id, db)
    except Exception:
        return raise_error(200001)


@router.post("/create-flower")
async def create_flower(flower: FlowerCreate, user=Depends(get_current_user), db=Depends(get_db)):
    try:
        if user is None:
            return raise_error(100002)
        if user.get("role") != "seller":
            return raise_error(1)
        return create(flower, db)
    except Exception:
        return raise_error(200002)


@router.put("/update-flower/{flower_id}")
async def update_flower(flower_update: FlowerCreate, flower_id: int, user=Depends(get_current_user), db=Depends(get_db)):
    try:
        if user is None:
            return raise_error(100002)
        if user.get("role") != "seller":
            return raise_error(1)
        return update(flower_id, flower_update, db)
    except Exception:
        return raise_error(200005)


@router.delete("/delete-flower/{flower_id}")
async def delete_flower(flower_id: int, user=Depends(get_current_user), db=Depends(get_db)):
    try:
        if user is None:
            return raise_error(100002)
        if user.get("role") != "seller":
            return raise_error(1)
        return delete(flower_id, db)
    except Exception:
        return raise_error(200006)