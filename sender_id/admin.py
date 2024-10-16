from django.contrib import admin
from .models import SenderIdAccount, SenderIdCustomer, SenderIdShared

@admin.register(SenderIdAccount)
class SenderIdAccountAdmin(admin.ModelAdmin):
    list_display = ('accountsenderid_id', 'created_date', 'senderid', 'update_date', 'accountname')
    search_fields = ('accountsenderid_id', 'accountname')

@admin.register(SenderIdCustomer)
class SenderIdCustomerAdmin(admin.ModelAdmin):
    list_display = ('customersenderid_id', 'created_date', 'senderid', 'update_date', 'customername')
    search_fields = ('customersenderid_id', 'customername')

@admin.register(SenderIdShared)
class SenderIdSharedAdmin(admin.ModelAdmin):
    list_display = ('senderid_id', 'created_date', 'senderid', 'update_date')
    search_fields = ('senderid_id', 'senderid')
