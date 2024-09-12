from fastapi import APIRouter, Depends
from exceptions import raise_error
from services.customer_service import get_all, get_by_id, create, daily_orders, monthly_orders, quarterly_orders, yearly_orders
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


@router.get("/get-daily-orders")
async def get_daily_orders(day: int, month: int, year: int, user=Depends(get_current_user), db=Depends(get_db)):
    try:
        if user is None:
            return raise_error(100002)
        if user.get("role") != "customer":
            return raise_error(2)
        return daily_orders(user.get("id"), day, month, year, db)
    except Exception:
        return raise_error(300001)


@router.get("/get-monthly-orders")
async def get_monthly_orders(month: int, year: int, user=Depends(get_current_user), db=Depends(get_db)):
    try:
        if user is None:
            return raise_error(100002)
        if user.get("role") != "customer":
            return raise_error(2)
        return monthly_orders(user.get("id"), month, year, db)
    except Exception:
        return raise_error(300001)


@router.get("/get-quarterly-orders")
async def get_quarterly_orders(quarter: int, year: int, user=Depends(get_current_user), db=Depends(get_db)):
    try:
        if user is None:
            return raise_error(100002)
        if user.get("role") != "customer":
            return raise_error(2)
        return quarterly_orders(user.get("id"), quarter, year, db)
    except Exception:
        return raise_error(300001)


@router.get("/get-yearly-orders")
async def get_yearly_orders(year: int, user=Depends(get_current_user), db=Depends(get_db)):
    try:
        if user is None:
            return raise_error(100002)
        if user.get("role") != "customer":
            return raise_error(2)
        return yearly_orders(user.get("id"), year, db)
    except Exception:
        return raise_error(300001)