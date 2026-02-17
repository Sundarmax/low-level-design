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
    def find_key_by_long_url(self, long_url : str) -> Optional[str]:
        pass

    @abstractmethod
    def get_next_id(self) -> int:
        pass

    @abstractmethod
    def exists_by_key(self, key: str) -> bool:
        pass
    

class InMemoryURLRepository(URLRepository):

    def __init__(self):
        self.key_to_url_map : dict[str, ShortenedURL] ={}
        self.long_url_to_key_map : dict[str, str] = {}
        self.id_counter = 0
        self._lock = Lock()

    def save(self, url: ShortenedURL) -> None:
        with self._lock:
            self.key_to_url_map[url.get_short_key()] = url
            self.long_url_to_key_map[url.get_long_url()] = url.get_short_key()
    
    def find_by_key(self, key : str):
        with self._lock:
            return self.key_to_url_map.get(key)
    

    def find_key_by_long_url(self, long_url : str):
        with self._lock:
            return self.find_key_by_long_url.get(long_url)
    
    def get_next_id(self):
        pass

    def exists_by_key(self, key: str) -> bool:
        with self._lock:
            return key in self.key_to_url_map