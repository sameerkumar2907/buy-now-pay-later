from fastapi import FastAPI, Body, HTTPException
from .user_manager import UserManager
from .purchase_manager import PurchaseManager
from .repayment_manager import RepaymentManager
from .report_manager import ReportManager

app = FastAPI()

# Initialize managers
user_manager = UserManager()
purchase_manager = PurchaseManager(user_manager)
repayment_manager = RepaymentManager()
report_manager = ReportManager(user_manager, purchase_manager)

@app.get("/")
def home():
    return "Welcome to buy-now-pay-later!"

@app.post("/register")
def register_user(
    user_id: str = Body(...), 
    credit_limit: float = Body(...)
):
    return user_manager.register_user(user_id, credit_limit)


@app.get("/credit/{user_id}")
def get_available_credit(user_id: str):
    return user_manager.get_available_credit(user_id)


@app.post("/purchase")
def make_purchase(
    user_id: str = Body(...),
    amount: float  = Body(...),
    emi_months: int = 0
  ):
    return purchase_manager.make_purchase(user_id, amount, emi_months)


@app.post("/payment")
def record_payment(user_id: str, amount: float):
    return repayment_manager.record_payment(user_id, amount)


@app.get("/reports/outstanding")
def get_outstanding_balance(user_id: str):
    return report_manager.get_outstanding_balance(user_id)


@app.get("/reports/history")
def get_repayment_history(user_id: str):
    return report_manager.get_repayment_history(user_id)
