from rest_framework import serializers
from .models import Prices


class PriceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Prices
        fields = ['id', 'from_currency_code', 'from_currency_name', 'to_currency_code',
                  'to_currency_name', 'exchange_rate', 'last_refreshed', 'time_zone', 'bid_price', 'ask_price']
