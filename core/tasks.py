from __future__ import absolute_import, unicode_literals
from django.http import HttpRequest
from celery import shared_task
from celery.utils.log import get_task_logger
# from .views import getPrices

import requests
import environ

env = environ.Env()
environ.Env.read_env()


logger = get_task_logger(__name__)


@shared_task
def add():
    # apikey = env('API_KEY')
    # url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey='+apikey
    # response = requests.get(url)
    # data = response.json()

    # priceDetails = data["Realtime Currency Exchange Rate"]
    # price = Prices()
    # price.from_currency_code = priceDetails["1. From_Currency Code"]
    # price.from_currency_name = priceDetails["2. From_Currency Name"]
    # price.to_currency_code = priceDetails["3. To_Currency Code"]
    # price.to_currency_name = priceDetails["4. To_Currency Name"]
    # price.exchange_rate = priceDetails["5. Exchange Rate"]
    # price.last_refreshed = priceDetails["6. Last Refreshed"]
    # price.time_zone = priceDetails["7. Time Zone"]
    # price.bid_price = priceDetails["8. Bid Price"]
    # price.ask_price = priceDetails["9. Ask Price"]
    # price.save()
    logger.info("The sample task just ran  from core folder.")
    print("hellooo.....333")
