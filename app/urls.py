from django.urls import path
from .views import PriceList

urlpatterns = [
    path('api/v1/quotes/', PriceList.as_view()),

]
