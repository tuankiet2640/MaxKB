# Service layer for user domain logic
from app.domain.models import User

class UserService:
    def get_user(self, user_id: int) -> User:
        # Placeholder for actual logic
        return User(id=user_id, username="test", email="test@example.com")
