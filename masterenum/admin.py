from django.contrib import admin
from .models import IPCheck, MNCMCCCheck, InvoiceType, Protocol, RouteCheck, RouteType, SenderIdCheck, SmsType, Status, PriceCheck

@admin.register(IPCheck)
class IPCheckAdmin(admin.ModelAdmin):
    list_display = ('ipcheck_id', 'type', 'update_date')
    search_fields = ('ipcheck_id', 'type')

@admin.register(MNCMCCCheck)
class MNCMCCCheckAdmin(admin.ModelAdmin):
    list_display = ('senderidcheck_id', 'type', 'update_date')
    search_fields = ('senderidcheck_id', 'type')

@admin.register(InvoiceType)
class InvoiceTypeAdmin(admin.ModelAdmin):
    list_display = ('invoicetype_id', 'invoicetype', 'update_date')
    search_fields = ('invoicetype_id', 'invoicetype')

@admin.register(Protocol)
class ProtocolAdmin(admin.ModelAdmin):
    list_display = ('senderidcheck_id', 'type', 'update_date')
    search_fields = ('senderidcheck_id', 'type')

@admin.register(RouteCheck)
class RouteCheckAdmin(admin.ModelAdmin):
    list_display = ('routecheck_id', 'type', 'update_date')
    search_fields = ('routecheck_id', 'type')

@admin.register(RouteType)
class RouteTypeAdmin(admin.ModelAdmin):
    list_display = ('routetype_id', 'type', 'update_date')
    search_fields = ('routetype_id', 'type')

@admin.register(SenderIdCheck)
class SenderIdCheckAdmin(admin.ModelAdmin):
    list_display = ('senderidcheck_id', 'type', 'update_date')
    search_fields = ('senderidcheck_id', 'type')

@admin.register(SmsType)
class SmsTypeAdmin(admin.ModelAdmin):
    list_display = ('smstype_id', 'smstype', 'update_date')
    search_fields = ('smstype_id', 'smstype')

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('senderidcheck_id', 'type', 'update_date')
    search_fields = ('senderidcheck_id', 'type')

@admin.register(PriceCheck)
class PriceCheckAdmin(admin.ModelAdmin):
    list_display = ('pricecheck_id', 'type', 'update_date')
    search_fields = ('pricecheck_id', 'type')
