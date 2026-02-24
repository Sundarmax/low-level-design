from .commentableEntity import CommentableEntity
from .user import User

class Comment(CommentableEntity):
    
    def __init__(self, author : User, content : str):
        super().__init__(author, content)