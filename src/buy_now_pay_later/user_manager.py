from fastapi import HTTPException

class UserManager:
    def __init__(self):
        self.users = {}  # Mock in-memory storage for users

    def register_user(self, user_id: str, credit_limit: float):
        if user_id in self.users:
            return {"error": "User already exists"}
        self.users[user_id] = {"credit_limit": credit_limit, "available_credit": credit_limit}
        print('users', self.users)
        return {"message": "User registered successfully", "user": self.users[user_id]}

    def get_available_credit(self, user_id: str):
        print('users', self.users)
        if user_id not in self.users:
            raise HTTPException(status_code=404, detail="User not found")
        return {"user_id": user_id, "available_credit": self.users[user_id]["available_credit"]}
