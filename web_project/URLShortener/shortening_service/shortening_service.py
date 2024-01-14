from URLShortener.shortening_strategy.shortening_strategy_interface import ShorteningStrategy

class URLShorteningService():
    def __init__(self, shortening_strategy: ShorteningStrategy):
        self.shortening_strategy = shortening_strategy
    
    def get_shortened_url(self, original_url):
        short_url = self.shortening_strategy.execute(original_url)
        return short_url

