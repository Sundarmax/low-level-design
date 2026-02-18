

from .observer import Observer
from enums.event_type import EventType

import threading

class AnalyticsService(Observer):

    def __init__(self):
        self._lock = threading.Lock()
        self.click_counts = {}
    
    def update(self, event_type, url):
        if event_type == EventType.URL_CREATED:
            with self._lock:
                self.click_counts[url.get_short_key()] = 0
            print(f"[Analytics] URL Created: Key={url.get_short_key()}, Original={url.get_long_url()}")
        elif event_type == EventType.URL_ACCESSED:
            with self._lock:
                if url.short_key() not in self.click_counts:
                    self.click_counts[url.short_key()] = 0
                self.click_counts[url.short_key()] += 1
                count = self.click_counts[url.short_key()]
            print(f"[Analytics] URL Accessed: Key={url.get_short_key()}, Clicks={count}")


