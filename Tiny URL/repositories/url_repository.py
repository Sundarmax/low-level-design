from abc import ABC,abstractmethod
from builder.shortened_url import ShortenedURL
from typing import Optional
from threading import Lock

class URLRepository(ABC):
    
    @abstractmethod
    def save(self, url: ShortenedURL) -> None:
        pass
    
    @abstractmethod
    def find_by_key(self, key:str) -> Optional[ShortenedURL]:
        pass
    
    @abstractmethod
    def find_key_by_long_url(self, long_url):
        pass

    @abstractmethod
    def get_next_id(self) -> int:
        pass

    @abstractmethod
    def exists_by_key(self, key: str) -> bool:
        pass
    
    @abstractmethod
    def print_key_values(self):
        pass
