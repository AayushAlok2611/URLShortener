from django.http import HttpResponse
from django. views. decorators. csrf import csrf_exempt
import json
# from constants import DEFAULT_SHORTENING_STRATEGY
from URLShortener.utils import get_shortening_strategy_obj
from URLShortener.shortening_service.shortening_service import URLShorteningService
from URLShortener.constants import ShorteningStrategyEnum

@csrf_exempt
def test_route(request):
    if request.method == 'GET':
        return HttpResponse("GET Request")

    if request.method == 'POST':
        return HttpResponse('POST Request')
    
    if request.method == 'DELETE':
        return HttpResponse('DELETE Request')
    
    return HttpResponse('Hello from URL Shortener App')

@csrf_exempt
def shorten_url(request):
    body = None
    url = None
    shortening_strategy = None

    # Doing this just to prove that for each type of HTTP request , data sent int the body , is present in request.body
    if request.method == 'GET':
        body = json.loads(request.body)
        url = body["url"]
        shortening_strategy = body.get("shortening_strategy", None)
        
    if request.method == 'POST':
        body = json.loads(request.body)
        url = body["url"]
        shortening_strategy = body.get("shortening_strategy", None)
    
    if request.method == 'DELETE':
        body = json.loads(request.body)
        url = body.get["url"]
        shortening_strategy = body.get("shortening_strategy", None)
    
    if shortening_strategy is None:
        shortening_strategy = ShorteningStrategyEnum.DefaultShorteningStrategy
    
    manualShortUrl = None
    if shortening_strategy == ShorteningStrategyEnum.ManualShorteningStrategy:
        manualShortUrl = body["manualShortUrl"]
    
    shortening_strategy_obj = get_shortening_strategy_obj(shortening_strategy, manualShortUrl=manualShortUrl)
    shortening_service = URLShorteningService(shortening_strategy=shortening_strategy_obj)
    short_url = shortening_service.get_shortened_url(url)

    return HttpResponse(f"The shortened url is : {short_url}")
