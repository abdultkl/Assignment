from django.urls import path
from .views import getPrices, PriceList

urlpatterns = [
    path('get_base_price', getPrices),
    path('api/v1/quotes/', PriceList.as_view()),

]
