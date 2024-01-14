from URLShortener.constants import ShorteningStrategyEnum
from URLShortener.shortening_strategy.default_shortening_strategy import DefaultShorteningStrategy
from URLShortener.shortening_strategy.manual_shortening_strategy import ManualShorteningStrategy
from URLShortener.shortening_strategy.shortening_strategy_interface import ShorteningStrategy

def get_shortening_strategy_obj(shortening_strategy: str, *args, **kwargs) -> ShorteningStrategy:
    if shortening_strategy == ShorteningStrategyEnum.ManualShorteningStrategy:
        manualShortUrl = kwargs["manualShortUrl"]
        return ManualShorteningStrategy(manualShortUrl)

    return DefaultShorteningStrategy()