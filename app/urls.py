from django.urls import path
from .views import getPrices

urlpatterns = [
    path('data', getPrices),
]
