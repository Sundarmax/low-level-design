
import threading
from entities.user import User
from typing import Optional
from entities.post import Post

class PostRepository:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.posts = {}
        return cls._instance
    
    @classmethod
    def get_instance(cls):
        return cls()
    
    def save(self, post : Post):
        self.post[post.get_id()] = post

    def find_by_id(self, post_id: str) -> Optional['Post']:
        return self.posts.get(post_id)
