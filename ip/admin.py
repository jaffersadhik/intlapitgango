from django.contrib import admin
from .models import IpAccount, IpCustomer, IpShared

@admin.register(IpAccount)
class IpAccountAdmin(admin.ModelAdmin):
    list_display = ('ipaccount_id', 'created_date', 'ip', 'update_date', 'accountname')
    search_fields = ('ipaccount_id', 'ip', 'accountname')

@admin.register(IpCustomer)
class IpCustomerAdmin(admin.ModelAdmin):
    list_display = ('ipcustomer_id', 'created_date', 'ip', 'update_date', 'customername')
    search_fields = ('ipcustomer_id', 'ip', 'customername')

@admin.register(IpShared)
class IpSharedAdmin(admin.ModelAdmin):
    list_display = ('ip_id', 'created_date', 'ip', 'update_date')
    search_fields = ('ip_id', 'ip')
