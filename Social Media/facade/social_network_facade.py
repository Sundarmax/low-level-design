
from services.post_service import PostService
from services.user_service import UserService
from entities.user import User

class SocialNetworkFacade:

    def __init__(self):
        self.user_service = UserService()
        self.post_service = PostService()
    
    def create_user(self,name: str, email: str) -> User:
        return self.user_service.create_user(name,email)
    
    def add_friend(self,user_id1: str, user_id2: str):
        return self.user_service.add_friend(user_id1,user_id2)
    
    def create_post(self, author : User, content: str):
        return self.post_service.create_post(author,content)
    
    def add_comment(self, author : User, post_id : str, content : str):
        return self.post_service.addComment(author,post_id,content)
    
    def like_post(self, user : User, post_id: str):
        return self.post_service.like_post(user, post_id)
    

