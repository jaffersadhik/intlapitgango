from django.contrib import admin
from .models import Payment, Invoice, Outstanding

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'amount', 'currency', 'payer_email', 'payment_date', 'payment_method', 'payment_status', 'transaction_id', 'customername')
    search_fields = ('payment_id', 'payer_email', 'transaction_id', 'customername')

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_id', 'created_date', 'invoice_date', 'invoice_period_end_date', 'invoice_period_start_date', 'invoiceamount', 'update_date', 'accountname')
    search_fields = ('invoice_id', 'accountname')

@admin.register(Outstanding)
class OutstandingAdmin(admin.ModelAdmin):
    list_display = ('outstanding_id', 'created_date', 'invoice_amount', 'invoice_period_year', 'outstanding_period_year', 'outstandingamount', 'payment_amount', 'payment_period_year', 'update_date', 'customername')
    search_fields = ('outstanding_id', 'customername')
