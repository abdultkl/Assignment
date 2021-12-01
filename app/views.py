from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Prices
from .serializers import PriceSerializers

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class PriceList(APIView):

    # fetching latest exchange prices
    def get(self, request, format=None):
        lastestExchangeRate = Prices.objects.last()
        serializer = PriceSerializers(lastestExchangeRate, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # fetching all prices
    def post(self, request, format=None):
        allPrices = Prices.objects.all()
        serializer = PriceSerializers(allPrices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
