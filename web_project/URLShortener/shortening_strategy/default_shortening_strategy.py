import hashlib
import base64
import random

from URLShortener.shortening_strategy.shortening_strategy_interface import ShorteningStrategy 

class DefaultShorteningStrategy(ShorteningStrategy):
    def execute(self, originalUrl):
        hashed_string = hashlib.sha256(originalUrl.encode('utf-8')).digest()
        b64 = base64.b64encode(hashed_string)
        b64= (b64.decode('utf-8'))
        shuffle = ''.join(random.sample(b64, len(b64)))
        final_url = shuffle.replace("/", "")
        final_url = final_url.replace("=","")
        return final_url[:7]