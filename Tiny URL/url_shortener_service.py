
from repositories.url_repository import InMemoryURLRepository,URLRepository
class URLShortenerService:

    def __init__(self):
        self.domain = None
        self.key_generation_strategy = None
        self.url_repository = None

    def configure(self, domain: str, repository: URLRepository, strategy : None ):
        self.domain = domain
        self.url_repository = repository
        self.key_generation_strategy = strategy

    def shorten(self, long_url: str):
        # check if shortened url exists
        existing_key = self.url_repository.find_key_by_long_url(long_url)
        if existing_key is not None:
            return self.domain + existing_key

        # generate a new URL

    def _generate_unique_key(self) -> str:
        pass