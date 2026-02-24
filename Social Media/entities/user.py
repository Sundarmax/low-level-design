
import uuid
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from repositories.post_repo import Post

class User:

    def __init__(self,name: str, email: str):
        self.id = str(uuid.uuid4())
        self.name =  name
        self.email = email
        self.posts : list['Post'] = []
        self.friends : set['User'] = set()

    def add_post(self, post: 'Post'):
        self.posts.append(post)

    def add_friend(self, friend : 'User'):
        self.friends.append(friend)

    # getter methods
    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email
    
    def get_posts(self):
        return self.posts
    
    def get_friends(self) -> set['User']:
        return self.friends
    
    def get_id(self):
        return self.id