from .news_feed_gen_strategy import NewsFeedGenerationStrategy
from entities.user import User

class ChronologicalStragey(NewsFeedGenerationStrategy):
    def generate_feed(self, user : User):
        friends = user.get_friends()
        feed = []
        for frd in friends:
            feed.extend(frd.get_posts())
        feed.sort(key=lambda p: p.get_timestamp(), reverse=True)
        return feed
    
