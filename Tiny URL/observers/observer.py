from abc import ABC,abstractmethod
from enums.event_type import EventType
from builder.shortened_url import ShortenedURL

class Observer(ABC):
    @abstractmethod
    def update(self, event_type : EventType, url : ShortenedURL ):
        pass
    
