from django.contrib import admin
from .models import WebhookAccount, WebhookCustomer, WebhookParameterIndex

@admin.register(WebhookAccount)
class WebhookAccountAdmin(admin.ModelAdmin):
    list_display = ('webhookaccount_id', 'created_date', 'date_format', 'postdata', 'update_date', 'weghookurl', 'accountname')
    search_fields = ('webhookaccount_id', 'accountname', 'date_format', 'postdata', 'weghookurl')

@admin.register(WebhookCustomer)
class WebhookCustomerAdmin(admin.ModelAdmin):
    list_display = ('webhookcustomer_id', 'created_date', 'date_format', 'postdata', 'update_date', 'weghookurl', 'customername')
    search_fields = ('webhookcustomer_id', 'customername', 'date_format', 'postdata', 'weghookurl')

@admin.register(WebhookParameterIndex)
class WebhookParameterIndexAdmin(admin.ModelAdmin):
    list_display = ('webhookparameter_id', 'created_date', 'indexnumber', 'parametername', 'update_date')
    search_fields = ('webhookparameter_id', 'parametername', 'indexnumber')
