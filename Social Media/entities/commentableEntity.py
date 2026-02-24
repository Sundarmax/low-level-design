
import uuid
from datetime import datetime
from .user import User
from .post import Post
from .comment import Comment

class CommentableEntity:

    def __init__(self, author : User, content: str):
        self.id = str(uuid.uuid4())
        self.author = author
        self.content = content
        self.timestamp = datetime.now()
        self.likes : set['User'] = set()
        self.comments : list['Comment'] = []

    def addLike(self, user : 'User'):
        self.likes.add(user)

    def addComment(self, cnt : 'Comment'):
        self.comments.append(cnt)

    # getter methods

    def get_id(self):
        return self.id
    
    def get_author(self):
        return self.author
    
    def get_content(self):
        return self.content
    
    def get_timestamp(self):
        return self.timestamp
    
    def get_comments(self) -> list['Comment']:
        return self.comments
    
    def get_likes(self) -> list['User']:
        return self.likes
    
    