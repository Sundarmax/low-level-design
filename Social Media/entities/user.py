
import uuid

class User:

    def __init__(self,name: str, email: str):
        self.id = str(uuid.uuid4())
        self.name =  name
        self.email = email
        self.posts : set['User'] = {}
        self.friends : list = []

    def addPost(self,):
        pass

    def addFriends(self, friend : 'User'):
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