from django.urls import path
from URLShortener import views

urlpatterns = [
    path("test", views.test_route),
    path("shorten_url",views.shorten_url)
]