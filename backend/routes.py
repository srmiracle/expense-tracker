from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Expense, User
from database import get_db
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Pydantic model for expense input validation
class ExpenseCreate(BaseModel):
    user_id: int
    category: str
    amount: float
    description: str = None

# Get all expenses
@router.get("/expenses", response_model=List[ExpenseCreate])
def get_expenses(db: Session = Depends(get_db)):
    return db.query(Expense).all()

# Add a new expense
@router.post("/expenses")
def add_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    new_expense = Expense(**expense.dict())
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

