from django.contrib import admin
from .models import (
    CostCarrier, 
    CostCarrierInvoiceDate, 
    CostCarrierMncmcc, 
    CostCarrierMncmccInvoiceDate, 
    CostSMSC, 
    CostSMSCInvoiceDate, 
    CostSMSCmncmcc, 
    CostSMSCmncmccInvoiceDate
)

@admin.register(CostCarrier)
class CostCarrierAdmin(admin.ModelAdmin):
    list_display = ('cost_id', 'cost', 'created_date', 'update_date', 'carriername', 'dial_in_code')
    search_fields = ('cost_id', 'carriername')

@admin.register(CostCarrierInvoiceDate)
class CostCarrierInvoiceDateAdmin(admin.ModelAdmin):
    list_display = ('cost_id', 'cost', 'created_date', 'invoice_date', 'update_date', 'carriername', 'dial_in_code')
    search_fields = ('cost_id', 'carriername')

@admin.register(CostCarrierMncmcc)
class CostCarrierMncmccAdmin(admin.ModelAdmin):
    list_display = ('cost_id', 'cost', 'created_date', 'mcc', 'mnc', 'update_date', 'carriername', 'dial_in_code')
    search_fields = ('cost_id', 'carriername')

@admin.register(CostCarrierMncmccInvoiceDate)
class CostCarrierMncmccInvoiceDateAdmin(admin.ModelAdmin):
    list_display = ('cost_id', 'cost', 'created_date', 'invoice_date', 'mcc', 'mnc', 'update_date', 'carriername', 'dial_in_code')
    search_fields = ('cost_id', 'carriername')

@admin.register(CostSMSC)
class CostSMSCAdmin(admin.ModelAdmin):
    list_display = ('cost_id', 'cost', 'created_date', 'update_date', 'dial_in_code', 'smscid')
    search_fields = ('cost_id', 'smscid')

@admin.register(CostSMSCInvoiceDate)
class CostSMSCInvoiceDateAdmin(admin.ModelAdmin):
    list_display = ('cost_id', 'cost', 'created_date', 'invoice_date', 'update_date', 'dial_in_code', 'smscid')
    search_fields = ('cost_id', 'smscid')

@admin.register(CostSMSCmncmcc)
class CostSMSCmncmccAdmin(admin.ModelAdmin):
    list_display = ('cost_id', 'cost', 'created_date', 'mcc', 'mnc', 'update_date', 'dial_in_code', 'smscid')
    search_fields = ('cost_id', 'smscid')

@admin.register(CostSMSCmncmccInvoiceDate)
class CostSMSCmncmccInvoiceDateAdmin(admin.ModelAdmin):
    list_display = ('cost_id', 'cost', 'created_date', 'invoice_date', 'mcc', 'mnc', 'update_date', 'dial_in_code', 'smscid')
    search_fields = ('cost_id', 'smscid')
