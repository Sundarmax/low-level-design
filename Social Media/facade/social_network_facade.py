from services.post_service import PostService
from services.user_service import UserService
from services.news_feed_service import NewsFeedService
from entities.user import User
from entities.post import Post
from observers.user_notifier import UserNotifier

class SocialNetworkFacade:
    def __init__(self):
        self.user_service = UserService()
        self.post_service = PostService()
        self.feed_service = NewsFeedService()
        self.post_service.observers.append(UserNotifier())
    
    def create_user(self,name: str, email: str) -> User:
        return self.user_service.create_user(name,email)
    
    def add_friend(self,user_id1: str, user_id2: str):
        return self.user_service.add_friend(user_id1,user_id2)
    
    def create_post(self, author_id: str, content: str):
        author =  self.user_service.get_user_by_id(author_id)
        return self.post_service.create_post(author,content)
    
    def add_comment(self, author : User, post_id : str, content : str):
        return self.post_service.addComment(author,post_id,content)
    
    def like_post(self, user_id: str, post_id: str):
        user = self.user_service.get_user_by_id(user_id)
        return self.post_service.like_post(user, post_id)

    def get_news_feed(self, user_id : str) -> list['Post']:
        user = self.user_service.get_user_by_id(user_id)
        return self.feed_service.get_news_feed(user)
    