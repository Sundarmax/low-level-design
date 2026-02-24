

from repositories.user_repo import UserRepository
from entities.user import User
from typing import Optional

class UserService:

    def __init__(self):
        self.user_repo = UserRepository.get_instance()

    def create_user(self, name: str, email: str) -> User:
        user = User(name, email)
        self.user_repo.save(user)
        return user
    
    def add_friend(self, user_id1 : str, user_id2 : str):
        user1 = self.user_repo.find_by_id(user_id1)
        user2 = self.user_repo.find_by_id(user_id2)
        user1.add_friend(user2)
        user2.add_friend(user1)
    
    def get_user_by_id(self, user_id : str) -> Optional[User]:
        return self.user_repo.find_by_id(user_id)
    
        
        
    
