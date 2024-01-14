from django.urls import path
from URLShortener import views

urlpatterns = [
    path("", views.home),
]