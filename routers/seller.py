from fastapi import APIRouter, Depends
from exceptions import raise_error
from services.seller_service import get_all_customers, get_all_customers_orders, daily_revenue, monthly_revenue, quarterly_revenue, yearly_revenue, get_all_loyal_customers, get_all_loyal_customers_by_tier
from configs.database import get_db
from configs.authentication import get_current_user
from schemas.customer_info import CustomerTier

router = APIRouter(
    prefix="/api/seller",
    tags=["Seller"]
)


@router.get("/get-customers")
async def get_customers(user=Depends(get_current_user), db=Depends(get_db)):
    try:
        if user is None:
            return raise_error(100002)
        if user.get("role") != "seller":
            return raise_error(1)
        return get_all_customers(db)
    except Exception:
        return raise_error(400001)


@router.get("/get-customers-orders")
async def get_customers_orders(user=Depends(get_current_user), db=Depends(get_db)):
    try:
        if user is None:
            return raise_error(100002)
        if user.get("role") != "seller":
            return raise_error(1)
        return get_all_customers_orders(db)
    except Exception:
        return raise_error(400001)
    

@router.get("/get-daily-revenue")
async def get_daily_revenue(day: int, month: int, year: int, user=Depends(get_current_user), db=Depends(get_db)):
    try:
        if user is None:
            return raise_error(100002)
        if user.get("role") != "seller":
            return raise_error(1)
        return daily_revenue(day, month, year, db)
    except Exception:
        return raise_error(400001)


@router.get("/get-monthly-revenue")
async def get_monthly_revenue(month: int, year: int, user=Depends(get_current_user), db=Depends(get_db)):
    try:
        if user is None:
            return raise_error(100002)
        if user.get("role") != "seller":
            return raise_error(1)
        return monthly_revenue(month, year, db)
    except Exception:
        return raise_error(400001)


@router.get("/get-quarterly-revenue")
async def get_quarterly_revenue(quarter: int, year: int, user=Depends(get_current_user), db=Depends(get_db)):
    try:
        if user is None:
            return raise_error(100002)
        if user.get("role") != "seller":
            return raise_error(1)
        return quarterly_revenue(quarter, year, db)
    except Exception:
        return raise_error(400001)


@router.get("/get-yearly-revenue")
async def get_yearly_revenue(year: int, user=Depends(get_current_user), db=Depends(get_db)):
    try:
        if user is None:
            return raise_error(100002)
        if user.get("role") != "seller":
            return raise_error(1)
        return yearly_revenue(year, db)
    except Exception:
        return raise_error(400001)


@router.get("/get-loyal-customers")
async def get_loyal_customers(user=Depends(get_current_user), db=Depends(get_db)):
    try:
        if user is None:
            return raise_error(100002)
        if user.get("role") != "seller":
            return raise_error(1)
        return get_all_loyal_customers(db)
    except Exception:
        return raise_error(400001)


@router.get("/get-loyal-customers-by-tier")
async def get_loyal_customers_by_tier(tier: CustomerTier, user=Depends(get_current_user), db=Depends(get_db)):
    try:
        if user is None:
            return raise_error(100002)
        if user.get("role") != "seller":
            return raise_error(1)
        return get_all_loyal_customers_by_tier(tier, db)
    except Exception:
        return raise_error(400001)