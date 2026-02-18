from repositories.url_repository import URLRepository
from repositories.in_memory_url_repo import InMemoryURLRepository
from strategies.key_gen_strategy import KeyGenerationStrategy
from builder.shortened_url import ShortenedURL
from observers.observer import Observer
from enums.event_type import EventType
import threading

class URLShortenerService:

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized') or not self._initialized:
            self.domain = None
            self.key_generation_strategy = None
            self.url_repository = None
            self._initialized = True
            self.observers : list[Observer] =[]

    @classmethod
    def get_instance(cls):
        return cls()

    def configure(self, domain: str, repository: URLRepository, strategy : KeyGenerationStrategy ):
        self.domain = domain
        self.url_repository = repository
        self.key_generation_strategy = strategy

    def shorten(self, long_url: str):
        # check if shortened url exists
        existing_key = self.url_repository.find_key_by_long_url(long_url)
        if existing_key is not None:
            return self.domain + existing_key
        
        # generate a new URL
        short_key = self._generate_unique_key()
        shortened_url = ShortenedURL.Builder(long_url,short_key).build()
        self.url_repository.save(shortened_url)
        # print(self.url_repository.print_key_values())
        self.notify_observer(EventType.URL_CREATED,shortened_url)
        return self.domain + short_key
    
    def _generate_unique_key(self) -> str:
        potential_key = self.key_generation_strategy.generate_key(
            self.url_repository.get_next_id()
        )
        if not self.url_repository.exists_by_key(potential_key):
            return potential_key        
    
    def add_observer(self, observer : Observer):
        self.observers.append(observer)

    def notify_observer(self, event_type : EventType, short_url : ShortenedURL):
        for observer in self.observers:
            observer.update(event_type,short_url)