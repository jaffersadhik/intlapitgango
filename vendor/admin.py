from django.contrib import admin
from .models import Carrier, SMSC

@admin.register(Carrier)
class CarrierAdmin(admin.ModelAdmin):
    list_display = ( 'carriername', 'companyname', 'created_date', 'email', 'phone', 'update_date')
    search_fields = ( 'carriername', 'companyname', 'email')

@admin.register(SMSC)
class SMSCAdmin(admin.ModelAdmin):
    list_display = ( 'created_date', 'ip', 'mode', 'password', 'port', 'securelevel', 'smscid', 'tps', 'update_date', 'username', 'carriername', 'dial_in_code', 'currencycode', 'routetype', 'smstype', 'timezone_id')
    search_fields = ( 'ip', 'mode', 'smscid', 'carriername', 'dial_in_code', 'currencycode', 'routetype', 'smstype', 'timezone_id')
