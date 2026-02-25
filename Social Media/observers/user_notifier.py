from .post_observer import PostObserver
from entities.user import User
from entities.post import Post

class UserNotifier(PostObserver):
    
    def on_like(self, post : Post, user : User):
        author = post.get_author()
        print(f"Notification for {author.get_name()} : {user.get_name()} liked your post")

    def on_post_created(self, post : Post):
        author = post.get_author()

        for friend in author.get_friends():
            print(f"Notification for {friend.get_name()}: {author.get_name()} created a new post: {post.get_content()}")
    
    def on_comment(self, post, user, comment):
        pass