from fastapi import HTTPException
from buy_now_pay_later.user_manager import UserManager


class PurchaseManager:
    def __init__(self, user_manager: UserManager):
        self.user_manager = user_manager
        self.purchases = []

    def make_purchase(self, user_id: str, amount: float, emi_months: int):
        user_data = self.user_manager.users.get(user_id)

        if not user_data:
            raise HTTPException(status_code=404, detail="User not found")

        if amount > user_data["available_credit"]:
            raise HTTPException(status_code=400, detail="Insufficient credit")

        # Deduct from credit and create purchase
        user_data["available_credit"] -= amount
        self.user_manager.users[user_id] = user_data
        purchase = {"user_id": user_id, "amount": amount, "emi_months": emi_months}
        self.purchases.append(purchase)

        return {"message": "Purchase recorded", "purchase": purchase}
