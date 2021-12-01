from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.http import HttpRequest

from app.views import getPrices


@shared_task
def add():
    print("hellooo.....4")
    getPrices(HttpRequest)
