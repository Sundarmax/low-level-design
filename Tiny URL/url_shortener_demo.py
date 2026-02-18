
from service.url_shortener_service import URLShortenerService
from repositories.in_memory_url_repo import InMemoryURLRepository
from strategies.uuid_strategy import UUIDStrategy
from observers.analytics_service import AnalyticsService

def main(): 
    
    shortener = URLShortenerService.get_instance()
    # configure
    shortener.configure("http://max.ly/", InMemoryURLRepository(),UUIDStrategy())
    # add observer
    shortener.add_observer(AnalyticsService())
    # shortener
    original_url1 = "https://www.verylongurl.com/with/lots/of/path/segments/and/query/params?id=123&user=test"
    print("Shortening: " + original_url1)
    tiny_url = shortener.shorten(original_url1)
    print("Generated short URL : ", tiny_url)
    
    # shortener - check duplicate request handling
    original_url2 = "https://www.verylongurl.com/with/lots/of/path/segments/and/query/params?id=123&user=test"
    print("Shortening: " + original_url2)
    tiny_url2 = shortener.shorten(original_url2)
    print("Generated short URL : ", tiny_url2)

    # shortener - new URL
    original_url3 = "https://www.newurl.com/with/lots/of/path/segments/and/query/params?id=123&user=test"
    print("Shortening: " + original_url3)
    tiny_url3 = shortener.shorten(original_url3)
    print("Generated short URL : ", tiny_url3)

main()
