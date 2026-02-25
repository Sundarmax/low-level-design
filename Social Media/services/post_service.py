
from repositories.post_repo import PostRepository
from entities.post import Post
from entities.user import User
from entities.comment import Comment
from observers.post_observer import PostObserver

class PostService:

    def __init__(self):
        self.post_repo = PostRepository.get_instance()
        self.observers :  list[PostObserver] = []

    def like_post(self, user : User , post_id : str):
        post = self.post_repo.find_by_id(post_id)
        post.addLike(User)
        # notify

    def create_post(self, author: User, cnt : str):
        post = Post(author, cnt)
        self.post_repo.save(post)
        author.add_post(post)
        for observer in self.observers:
            observer.on_post_created(post)
        return post
    
    def addComment(self, author : User, cnt_id : str, content: str):
        new_comment = Comment(author, content) 
        post = self.post_repo.find_by_id(cnt_id)
        post.addComment(new_comment)
        # notify
