from fastapi import HTTPException


class RepaymentManager:
    def __init__(self):
        self.repayments = []  # Mock in-memory storage for repayments

    def record_payment(self, user_id: str, amount: float):
        from .user_manager import UserManager

        user_manager = UserManager()
        user_data = user_manager.users.get(user_id)

        if not user_data:
            raise HTTPException(status_code=404, detail="User not found")

        # Add amount back to available credit
        user_data["available_credit"] += amount

        # Record repayment
        repayment = {"user_id": user_id, "amount": amount}
        self.repayments.append(repayment)

        return {"message": "Payment recorded successfully", "repayment": repayment}
