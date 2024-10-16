from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from datetime import datetime
from .models import Currency, CurrencyConversion, CurrencyConversionInvoiceDate
from .serializers import CurrencySerializer, CurrencyConversionSerializer, CurrencyConversionInvoiceDateSerializer

# Currency Views
class CurrencyListView(APIView):
    def get(self, request):
        currencies = Currency.objects.all()
        serializer = CurrencySerializer(currencies, many=True)
        return Response(serializer.data)

class CurrencyCreateView(APIView):
    def post(self, request):
        data = request.data.copy()
        data['created_date'] = datetime.now().isoformat()
        serializer = CurrencySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CurrencyUpdateView(APIView):
    def post(self, request):
        data = request.data.copy()
        currency_id = data.get('currency_id')
        if not currency_id:
            return Response({'detail': 'currency_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)
        
        currency = get_object_or_404(Currency, pk=currency_id)
        serializer = CurrencySerializer(currency, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Currency Conversion Views
class CurrencyConversionListView(APIView):
    def get(self, request):
        conversions = CurrencyConversion.objects.all()
        serializer = CurrencyConversionSerializer(conversions, many=True)
        return Response(serializer.data)

class CurrencyConversionCreateView(APIView):
    def post(self, request):
        data = request.data.copy()
        data['created_date'] = datetime.now().isoformat()
        data['update_date'] = datetime.now().isoformat()
        serializer = CurrencyConversionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CurrencyConversionUpdateView(APIView):
    def post(self, request):
        data = request.data.copy()
        currencyconversion_id = data.get('currencyconversion_id')
        if not currencyconversion_id:
            return Response({'detail': 'currencyconversion_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)
        
        conversion = get_object_or_404(CurrencyConversion, pk=currencyconversion_id)
        serializer = CurrencyConversionSerializer(conversion, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Currency Conversion Invoice Date Views
class CurrencyConversionInvoiceDateListView(APIView):
    def get(self, request):
        conversions = CurrencyConversionInvoiceDate.objects.all()
        serializer = CurrencyConversionInvoiceDateSerializer(conversions, many=True)
        return Response(serializer.data)

class CurrencyConversionInvoiceDateCreateView(APIView):
    def post(self, request):
        data = request.data.copy()
        data['created_date'] = datetime.now().isoformat()
        data['update_date'] = datetime.now().isoformat()
        serializer = CurrencyConversionInvoiceDateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CurrencyConversionInvoiceDateUpdateView(APIView):
    def post(self, request):
        data = request.data.copy()
        currencyconversion_id = data.get('currencyconversion_id')
        if not currencyconversion_id:
            return Response({'detail': 'currencyconversion_id is required for update.'}, status=status.HTTP_400_BAD_REQUEST)
        
        conversion = get_object_or_404(CurrencyConversionInvoiceDate, pk=currencyconversion_id)
        serializer = CurrencyConversionInvoiceDateSerializer(conversion, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
