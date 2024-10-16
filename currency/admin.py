from django.contrib import admin
from .models import Currency, CurrencyConversion, CurrencyConversionInvoiceDate

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('currency_id', 'currencycode', 'currencyname', 'territory', 'created_date', 'update_date')
    search_fields = ('currency_id', 'currencycode', 'currencyname')

@admin.register(CurrencyConversion)
class CurrencyConversionAdmin(admin.ModelAdmin):
    list_display = ('currencyconversion_id', 'conversionrate', 'created_date', 'update_date', 'from_currency', 'to_currency')
    search_fields = ('currencyconversion_id', 'from_currency', 'to_currency')

@admin.register(CurrencyConversionInvoiceDate)
class CurrencyConversionInvoiceDateAdmin(admin.ModelAdmin):
    list_display = ('currencyconversion_id', 'conversionrate', 'created_date', 'invoice_date', 'update_date', 'from_currency', 'to_currency')
    search_fields = ('currencyconversion_id', 'from_currency', 'to_currency')
