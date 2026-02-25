
from abc import ABC,abstractmethod
from entities.user import User

class NewsFeedGenerationStrategy(ABC):

    @abstractmethod
    def generate_feed(self, user : User ):
        pass