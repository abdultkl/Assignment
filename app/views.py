from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests

from .models import Prices
from .serializers import PriceSerializers


# Create your views here.


def getPrices(request):
    apikey = "IQKFCT1ET8PKDXD"
    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey='+apikey
    r = requests.get(url)
    data = r.json()

    priceDetails = data["Realtime Currency Exchange Rate"]
    price = Prices()
    price.from_currency_code = priceDetails["1. From_Currency Code"]
    price.from_currency_name = priceDetails["2. From_Currency Name"]
    price.to_currency_code = priceDetails["3. To_Currency Code"]
    price.to_currency_name = priceDetails["4. To_Currency Name"]
    price.exchange_rate = priceDetails["5. Exchange Rate"]
    price.last_refreshed = priceDetails["6. Last Refreshed"]
    price.time_zone = priceDetails["7. Time Zone"]
    price.bid_price = priceDetails["8. Bid Price"]
    price.ask_price = priceDetails["9. Ask Price"]
    if price.save():
        print("data saved")
        print(data)
        return HttpResponse("Saved record")
    else:
        print("Failed to save record")
        return HttpResponse("Failed to save")


def getLatestExchangeRates(request):
    lastestExchangeRate = Prices.objects.last()
    serializer = PriceSerializers(lastestExchangeRate, many=False)
    return JsonResponse(serializer.data, safe=False)
