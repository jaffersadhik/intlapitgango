from django.contrib import admin
from .models import ErrorcodeAccount, ErrorcodeCarrier, ErrorcodePlatform

@admin.register(ErrorcodeAccount)
class ErrorcodeAccountAdmin(admin.ModelAdmin):
    list_display = ('errorcode_id', 'created_date', 'platformerrorcode', 'update_date', 'accountname','errorcode','status')
    search_fields = ('errorcode_id', 'accountname')

@admin.register(ErrorcodeCarrier)
class ErrorcodeCarrierAdmin(admin.ModelAdmin):
    list_display = ('errorcode_id', 'created_date', 'description', 'errorcode', 'platformerrorcode', 'status', 'update_date', 'carriername')
    search_fields = ('errorcode_id', 'errorcode', 'platformerrorcode', 'carriername')

@admin.register(ErrorcodePlatform)
class ErrorcodePlatformAdmin(admin.ModelAdmin):
    list_display = ('errorcode_id', 'created_date', 'description', 'errorcode', 'status', 'update_date')
    search_fields = ('errorcode_id', 'errorcode')
