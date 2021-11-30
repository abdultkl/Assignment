from django.db import models

# Create your models here.

class Prices(models.Model):

    from_currency_code = models.CharField(max_length=20)
    from_currency_name = models.CharField(max_length=20)
    to_currency_code = models.CharField(max_length=20)
    to_currency_name = models.CharField(max_length=20)
    exchange_rate = models.DecimalField(max_digits=18,decimal_places=8)
    last_refreshed = models.DateTimeField()
    time_zone = models.CharField(max_length=10)
    bid_price = models.DecimalField(max_digits=18,decimal_places=8)
    ask_price = models.DecimalField(max_digits=18,decimal_places=8)

    class Meta:
        db_table = "prices"

    