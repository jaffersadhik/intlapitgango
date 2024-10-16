from django.contrib import admin
from .models import Account, Company, Customer

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'account_id', 'emailstatus', 'first_name', 'last_name', 'username', 'created_date'
    )
    search_fields = ('account_id', 'emailstatus', 'username')
    list_filter = ('status', 'created_date')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'company_id', 'fullname', 'email', 'mobilenumber', 'create_date'
    )
    search_fields = ('company_id', 'fullname', 'email')
    list_filter = ('activestatus', 'create_date')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'customer_id', 'customername', 'email', 'mobile', 'created_date'
    )
    search_fields = ('customer_id', 'customername', 'email')
    list_filter = ('invoicetype', 'created_date')
