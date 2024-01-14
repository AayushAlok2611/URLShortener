from URLShortener.shortening_strategy.shortening_strategy_interface import ShorteningStrategy

class ManualShorteningStrategy(ShorteningStrategy):
    def __init__(self, manualShortUrl):
        self.manualShortUrl = manualShortUrl
    
    def execute(self, originalUrl):
        return self.manualShortUrl
        
