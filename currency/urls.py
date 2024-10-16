from django.urls import path
from .views import (
    CurrencyListView, CurrencyCreateView, CurrencyUpdateView,
    CurrencyConversionListView, CurrencyConversionCreateView, CurrencyConversionUpdateView,
    CurrencyConversionInvoiceDateListView, CurrencyConversionInvoiceDateCreateView, CurrencyConversionInvoiceDateUpdateView
)

urlpatterns = [
    # Currency URLs
    path('currency/getall', CurrencyListView.as_view(), name='currency-getall'),
    path('currency/save', CurrencyCreateView.as_view(), name='currency-create'),
    path('currency/edit', CurrencyUpdateView.as_view(), name='currency-update'),

    # Currency Conversion URLs
    path('currencyconversion/getall', CurrencyConversionListView.as_view(), name='currencyconversion-getall'),
    path('currencyconversion/save', CurrencyConversionCreateView.as_view(), name='currencyconversion-create'),
    path('currencyconversion/edit', CurrencyConversionUpdateView.as_view(), name='currencyconversion-update'),

    # Currency Conversion Invoice Date URLs
    path('currencyconversioninvoicedate/getall', CurrencyConversionInvoiceDateListView.as_view(), name='currencyconversioninvoicedate-getall'),
    path('currencyconversioninvoicedate/save', CurrencyConversionInvoiceDateCreateView.as_view(), name='currencyconversioninvoicedate-create'),
    path('currencyconversioninvoicedate/edit', CurrencyConversionInvoiceDateUpdateView.as_view(), name='currencyconversioninvoicedate-update'),
]
