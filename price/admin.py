from django.contrib import admin
from .models import (
    PriceAccount, PriceAccountInvoiceDate, PriceAccountMncmcc, PriceAccountMncmccInvoiceDate,
    PriceCustomer, PriceCustomerInvoiceDate, PriceCustomerMncmcc, PriceCustomerMncmccInvoiceDate,
    PriceShared, PriceSharedInvoiceDate, PriceSharedMncmcc, PriceSharedMncmccInvoiceDate
)

@admin.register(PriceAccount)
class PriceAccountAdmin(admin.ModelAdmin):
    list_display = ('price_id', 'created_date', 'price', 'update_date', 'accountname', 'dial_in_code')
    search_fields = ('price_id', 'accountname')

@admin.register(PriceAccountInvoiceDate)
class PriceAccountInvoiceDateAdmin(admin.ModelAdmin):
    list_display = ('price_id', 'created_date', 'invoice_date', 'price', 'update_date', 'accountname', 'dial_in_code')
    search_fields = ('price_id', 'accountname')

@admin.register(PriceAccountMncmcc)
class PriceAccountMncmccAdmin(admin.ModelAdmin):
    list_display = ('price_id', 'created_date', 'mcc', 'mnc', 'price', 'update_date', 'accountname', 'dial_in_code')
    search_fields = ('price_id', 'accountname')

@admin.register(PriceAccountMncmccInvoiceDate)
class PriceAccountMncmccInvoiceDateAdmin(admin.ModelAdmin):
    list_display = ('price_id', 'created_date', 'invoice_date', 'mcc', 'mnc', 'price', 'update_date', 'accountname', 'dial_in_code')
    search_fields = ('price_id', 'accountname')

@admin.register(PriceCustomer)
class PriceCustomerAdmin(admin.ModelAdmin):
    list_display = ('price_id', 'created_date', 'price', 'update_date', 'dial_in_code', 'customername')
    search_fields = ('price_id', 'customername')

@admin.register(PriceCustomerInvoiceDate)
class PriceCustomerInvoiceDateAdmin(admin.ModelAdmin):
    list_display = ('price_id', 'created_date', 'invoice_date', 'price', 'update_date', 'dial_in_code', 'customername')
    search_fields = ('price_id', 'customername')

@admin.register(PriceCustomerMncmcc)
class PriceCustomerMncmccAdmin(admin.ModelAdmin):
    list_display = ('price_id', 'created_date', 'mcc', 'mnc', 'price', 'update_date', 'dial_in_code', 'customername')
    search_fields = ('price_id', 'customername')

@admin.register(PriceCustomerMncmccInvoiceDate)
class PriceCustomerMncmccInvoiceDateAdmin(admin.ModelAdmin):
    list_display = ('price_id', 'created_date', 'invoice_date', 'mcc', 'mnc', 'price', 'update_date', 'dial_in_code', 'customername')
    search_fields = ('price_id', 'customername')

@admin.register(PriceShared)
class PriceSharedAdmin(admin.ModelAdmin):
    list_display = ('price_id', 'created_date', 'price', 'update_date', 'dial_in_code')
    search_fields = ('price_id',)

@admin.register(PriceSharedInvoiceDate)
class PriceSharedInvoiceDateAdmin(admin.ModelAdmin):
    list_display = ('price_id', 'created_date', 'invoice_date', 'price', 'update_date', 'dial_in_code')
    search_fields = ('price_id',)

@admin.register(PriceSharedMncmcc)
class PriceSharedMncmccAdmin(admin.ModelAdmin):
    list_display = ('price_id', 'created_date', 'mcc', 'mnc', 'price', 'update_date', 'dial_in_code')
    search_fields = ('price_id',)

@admin.register(PriceSharedMncmccInvoiceDate)
class PriceSharedMncmccInvoiceDateAdmin(admin.ModelAdmin):
    list_display = ('price_id', 'created_date', 'invoice_date', 'mcc', 'mnc', 'price', 'update_date', 'dial_in_code')
    search_fields = ('price_id',)
