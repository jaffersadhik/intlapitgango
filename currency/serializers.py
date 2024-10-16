from rest_framework import serializers
from .models import Currency, CurrencyConversion, CurrencyConversionInvoiceDate

# Currency Serializer
class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'

# Currency Conversion Serializer
class CurrencyConversionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyConversion
        fields = '__all__'

# Currency Conversion Invoice Date Serializer
class CurrencyConversionInvoiceDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyConversionInvoiceDate
        fields = '__all__'
