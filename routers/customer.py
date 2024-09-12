from fastapi import APIRouter, Depends
from exceptions import raise_error
from services.customer_service import get_all, get_by_id, create
from configs.database import get_db
from configs.authentication import get_current_user
from schemas.order import OrderCreate

router = APIRouter(
    prefix="/api/customer",
    tags=["Customer"]
)


@router.get("/get-orders")
async def get_orders(user=Depends(get_current_user), db=Depends(get_db)):
    try:
        if user is None:
            return raise_error(100002)
        if user.get("role") != "customer":
            return raise_error(2)
        return get_all(user.get("id"), db)
    except Exception:
        return raise_error(300001)


@router.get("/get-order-by-id/{order_id}")
async def get_order_by_id(order_id: int, user=Depends(get_current_user), db=Depends(get_db)):
    try:
        if user is None:
            return raise_error(100002)
        if user.get("role") != "customer":
            return raise_error(2)
        return get_by_id(user.get("id"), order_id, db)
    except Exception:
        return raise_error(300001)


@router.post("/create-order")
async def create_order(order: OrderCreate, user=Depends(get_current_user), db=Depends(get_db)):
    try:
        if user is None:
            return raise_error(100002)
        if user.get("role") != "customer":
            return raise_error(2)
        return create(user.get("id"), order, db)
    except Exception:
        return raise_error(300002)