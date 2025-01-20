from buy_now_pay_later.user_manager import UserManager
from buy_now_pay_later.purchase_manager import PurchaseManager

class ReportManager:
    def __init__(self, user_manager: UserManager, purchase_manager: PurchaseManager):
        self.user_manager = user_manager
        self.purchase_manager = purchase_manager
        self.outstanding_balances = {}

    def get_outstanding_balance(self, user_id: str):
        from .purchase_manager import PurchaseManager
        purchase_manager = PurchaseManager(self.user_manager)

        print('users - ', self.user_manager.users)
        user_data = self.user_manager.users.get(user_id)
        print('user_data -- ', user_data)
        print('purchase_manager.purchases - ', self.purchase_manager.purchases)
        if not user_data:
            return {"error": "User not found"}

        outstanding = sum(
            purchase["amount"]
            for purchase in self.purchase_manager.purchases
            if purchase["user_id"] == user_id
        )
        return {"user_id": user_id, "outstanding_balance": outstanding}

    def get_repayment_history(self, user_id: str):
        from .repayment_manager import RepaymentManager

        repayment_manager = RepaymentManager()

        history = [
            repayment
            for repayment in repayment_manager.repayments
            if repayment["user_id"] == user_id
        ]

        if not history:
            return {"user_id": user_id, "repayment_history": "No repayments found"}

        return {"user_id": user_id, "repayment_history": history}
