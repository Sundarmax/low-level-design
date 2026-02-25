
from strategies.chronological_strategy import ChronologicalStragey
from strategies.news_feed_gen_strategy import NewsFeedGenerationStrategy
from entities.user import User
from entities.post import Post

class NewsFeedService:
    
    def __init__(self):
        self.strategy = ChronologicalStragey()
    
    def set_strategy(self, strgy : NewsFeedGenerationStrategy):
        self.strategy = strgy
    
    def get_news_feed(self, user : User) -> list['Post']:
        return self.strategy.generate_feed(user)

