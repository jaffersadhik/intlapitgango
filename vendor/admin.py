from django.contrib import admin
from .models import Carrier, SMSC

@admin.register(Carrier)
class CarrierAdmin(admin.ModelAdmin):
    list_display = ( 'carriername', 'companyname', 'created_date', 'email', 'phone', 'update_date')
    search_fields = ( 'carriername', 'companyname', 'email')

@admin.register(SMSC)
class SMSCAdmin(admin.ModelAdmin):
    list_display = ('created_date', 'smscid', 'carriername', 'routetype', 'dial_in_code', 'currencycode', 'smstype', 'timezone_id', 'mode')
    search_fields = ('smscid', 'carriername', 'dial_in_code', 'currencycode', 'routetype', 'smstype', 'timezone_id')
