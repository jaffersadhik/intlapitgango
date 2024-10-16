from django.contrib import admin
from .models import (
    Route,
    RouteAccount,
    RouteAccountMncmcc,
    RouteCustomer,
    RouteCustomerMncMcc,
    RouteShared,
    RouteSharedMncmcc
)

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('route_id', 'routename', 'update_date','created_date')
    search_fields = ('route_id', 'routename')

@admin.register(RouteAccount)
class RouteAccountAdmin(admin.ModelAdmin):
    list_display = (
        'routemapping_id', 'created_date', 'update_date', 'weight',
        'accountname', 'dial_in_code', 'routename', 'smscid'
    )
    search_fields = ('routemapping_id', 'accountname')

@admin.register(RouteAccountMncmcc)
class RouteAccountMncmccAdmin(admin.ModelAdmin):
    list_display = (
        'routemapping_id', 'created_date', 'mcc', 'mnc', 'update_date',
        'weight', 'accountname', 'dial_in_code', 'routename', 'smscid'
    )
    search_fields = ('routemapping_id', 'accountname')

@admin.register(RouteCustomer)
class RouteCustomerAdmin(admin.ModelAdmin):
    list_display = (
        'routemapping_id', 'created_date', 'update_date', 'weight',
        'dial_in_code', 'customername', 'routename', 'smscid'
    )
    search_fields = ('routemapping_id', 'customername')

@admin.register(RouteCustomerMncMcc)
class RouteCustomerMncMccAdmin(admin.ModelAdmin):
    list_display = (
        'routemapping_id', 'created_date', 'mcc', 'mnc', 'update_date',
        'weight', 'dial_in_code', 'customername', 'routename', 'smscid'
    )
    search_fields = ('routemapping_id', 'customername')

@admin.register(RouteShared)
class RouteSharedAdmin(admin.ModelAdmin):
    list_display = (
        'routemapping_id', 'created_date', 'update_date', 'weight',
        'dial_in_code', 'routename', 'smscid'
    )
    search_fields = ('routemapping_id', 'routename')

@admin.register(RouteSharedMncmcc)
class RouteSharedMncmccAdmin(admin.ModelAdmin):
    list_display = (
        'routemapping_id', 'created_date', 'mcc', 'mnc', 'update_date',
        'weight', 'dial_in_code', 'routename', 'smscid'
    )
    search_fields = ('routemapping_id', 'routename')
