
from service.url_shortener_service import URLShortenerService
from repositories.in_memory_url_repo import InMemoryURLRepository
from strategies.uuid_strategy import UUIDStrategy

def main(): 
    
    shortener = URLShortenerService.get_instance()
    # configure
    shortener.configure("http://max.ly/", InMemoryURLRepository(),UUIDStrategy())
    # shortener
    original_url1 = "https://www.verylongurl.com/with/lots/of/path/segments/and/query/params?id=123&user=test"
    print("Shortening: " + original_url1)
    tiny_url = shortener.shorten(original_url1)
    print("Generated short URL : ", tiny_url)

main()
