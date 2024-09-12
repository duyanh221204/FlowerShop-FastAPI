from exceptions import raise_error
from schemas.base_response import BaseResponse
from schemas.customer_info import CustomerInfo, CustomerOrder, CustomerTier
from schemas.order import OrderResponse, OrderDetailResponse
from models.user import User
from models.order import Order
from models.orderdetail import OrderDetail
from models.customerspending import CustomerSpending
from typing import List
from sqlalchemy.orm import Session
from services.get_tier import get_tier
from datetime import date
from sqlalchemy import func


def get_all_customers(db: Session) -> List[CustomerInfo]:
    info_model = db.query(User).filter(User.role == "customer").all()
    return [
        CustomerInfo(
            id=info.id,
            username=info.username,
            email=info.email,
            first_name=info.first_name,
            last_name=info.last_name,
            role=info.role,
            total_spending=info.spending.total_spending,
            tier=get_tier(info.spending.total_spending)
        )
        for info in info_model
    ]


def get_all_customers_orders(db: Session) -> List[CustomerOrder]:
    info_model = db.query(User).filter(User.role == "customer").all()
    response = []
    for info in info_model:
        orders = db.query(Order).filter(Order.user_id == info.id).all()
        orders_reponse = []
        for order in orders:
            order_details = db.query(OrderDetail).filter(OrderDetail.order_id == order.id).all()
            order_details_response = [
                OrderDetailResponse(
                    id=detail.id,
                    flower_id=detail.flower_id,
                    quantity=detail.quantity,
                    total_price=detail.total_price
                )
                for detail in order_details
            ]
            orders_reponse.append(
                OrderResponse(
                    id=order.id,
                    total_cost=order.total_cost,
                    day=order.day,
                    month=order.month,
                    year=order.year,
                    order_details=order_details_response
                )
            )
        response.append(
            CustomerOrder(
                user_id=info.id,
                username=info.username,
                total_spending=info.spending.total_spending,
                orders=orders_reponse
            )
        )
    return response


def daily_revenue(day: int, month: int, year: int, db: Session) -> dict | BaseResponse:
    try:
        date(year, month, day)
    except Exception:
        return raise_error(500001)
    total_revenue = db.query(func.sum(Order.total_cost)).filter(
        Order.day == day,
        Order.month == month,
        Order.year == year
    ).scalar() or 0
    return {
        "date": f"{day:02d}/{month:02d}/{year}",
        "revenue": total_revenue
    }


def monthly_revenue(month: int, year: int, db: Session) -> dict | BaseResponse:
    try:
        date(year, month, 1)
    except Exception:
        return raise_error(500001)
    total_revenue = db.query(func.sum(Order.total_cost)).filter(
        Order.month == month,
        Order.year == year
    ).scalar() or 0
    return {
        "month": f"{month:02d}/{year}",
        "revenue": total_revenue
    }


def quarterly_revenue(quarter: int, year: int, db: Session) -> dict | BaseResponse:
    if year < 0:
        return raise_error(10)
    if not 1 <= quarter <= 4:
        return raise_error(11)
    start_month, end_month = quarter * 3 - 2, quarter * 3
    total_revenue = db.query(func.sum(Order.total_cost)).filter(
        Order.month >= start_month,
        Order.month <= end_month,
        Order.year == year
    ).scalar() or 0
    return {
        "quarter": f"Q{quarter:02d}/{year}",
        "revenue": total_revenue
    }


def yearly_revenue(year: int, db: Session) -> dict | BaseResponse:
    if year < 0:
        return raise_error(10)
    total_revenue = db.query(func.sum(Order.total_cost)).filter(Order.year == year).scalar() or 0
    return {
        "year": year,
        "revenue": total_revenue
    }


def get_all_loyal_customers(db: Session) -> List[CustomerInfo]:
    loyal_customers = db.query(CustomerSpending).filter(CustomerSpending.total_spending >= int(5e5)).all()
    return [
        CustomerInfo(
            id=customer.id,
            username=customer.user.username,
            email=customer.user.email,
            first_name=customer.user.first_name,
            last_name=customer.user.last_name,
            role=customer.user.role,
            total_spending=customer.total_spending,
            tier=get_tier(customer.total_spending)
        )
        for customer in loyal_customers
    ]


def get_all_loyal_customers_by_tier(tier: CustomerTier, db: Session) -> List[CustomerInfo]:
    if tier == CustomerTier.bronze:
        min_spend, max_spend = int(5e5), int(1e6) - 1
    elif tier == CustomerTier.silver:
        min_spend, max_spend = int(1e6), int(1.5e6) - 1
    elif tier == CustomerTier.gold:
        min_spend, max_spend = int(1.5e6), int(2e6) - 1
    else:
        min_spend, max_spend = int(2e6), float("inf")
    query = db.query(CustomerSpending)
    if max_spend == float("inf"):
        customers_tier = query.filter(CustomerSpending.total_spending >= min_spend).all()
    else:
        customers_tier = query.filter(
            CustomerSpending.total_spending >= min_spend,
            CustomerSpending.total_spending <= max_spend
        ).all()
    return [
        CustomerInfo(
            id=customer.id,
            username=customer.user.username,
            email=customer.user.email,
            first_name=customer.user.first_name,
            last_name=customer.user.last_name,
            role=customer.user.role,
            total_spending=customer.total_spending,
            tier=get_tier(customer.total_spending)
        )
        for customer in customers_tier
    ]