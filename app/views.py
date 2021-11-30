from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests


# Create your views here.


def getPrices(request):
    apikey = "IQKFCT1ET8PKDXD"
    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey='+apikey
    r = requests.get(url)
    data = r.json()
    print(data)
    return HttpResponse(data)