from django.urls import path
from .views import getPrices, getLatestExchangeRates

urlpatterns = [
    path('get_base_price', getPrices),
    path('/api/v1/quotes', getLatestExchangeRates),

]
