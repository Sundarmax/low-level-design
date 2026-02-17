
from datetime import datetime

class ShortenedURL:

    def __init__(self,builder):
        self.long_url = builder.long_url
        self.short_key = builder.short_key
        self.creation_date = builder.creation_date

    def get_long_url(self):
        return self.long_url

    def get_short_key(self):
        return self.short_key

    def get_creation_date(self):
        self.creation_date

    class Builder:

        def __init__(self,long_url: str, short_key: str):
            self.long_url = long_url
            self.short_key = short_key
            self.creation_date = datetime.now()
        
        def creation_date(self, creation_date : datetime):
            self.creation_date = creation_date
            return self
        
        def build(self) -> 'ShortenedURL':
            return ShortenedURL(self)
        