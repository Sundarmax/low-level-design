
import threading
from entities.user import User
from typing import Optional

class UserRepository:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.users = {}
        return cls._instance
    
    @classmethod
    def get_instance(cls):
        return cls()
    
    def save(self, user : User):
        self.users[user.get_id()] = user
    

    def find_by_id(self, user_id: str) -> Optional['User']:
        return self.users.get(user_id)
