from django.contrib import admin
from .models import Country, MncMcc, MncMccPrefix, WorldTimezone

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_id', 'country', 'country_code_iso2', 'country_code_iso3', 'country_code_iso_numeric', 
                    'country_short_name', 'dial_in_code', 'dial_in_code_full', 'max_mobile_length', 'min_mobile_length', 'created_date', 'update_date')
    search_fields = ('country_id', 'country', 'country_code_iso2', 'country_code_iso3')

@admin.register(MncMcc)
class MncMccAdmin(admin.ModelAdmin):
    list_display = ('mncmcc_id', 'created_date', 'mcc', 'mnc', 'networkoperatorname', 'update_date', 'dial_in_code')
    search_fields = ('mncmcc_id', 'networkoperatorname')

@admin.register(MncMccPrefix)
class MncMccPrefixAdmin(admin.ModelAdmin):
    list_display = ('mccmncprefix_id', 'countrycode', 'mcc', 'mnc', 'prefix', 'update_date')
    search_fields = ('mccmncprefix_id', 'countrycode', 'mcc', 'mnc')

@admin.register(WorldTimezone)
class WorldTimezoneAdmin(admin.ModelAdmin):
    list_display = ('timezone_id', 'created_date', 'displayname', 'longname', 'offset', 'shortname', 'update_date', 'zonename')
    search_fields = ('timezone_id', 'displayname', 'longname', 'zonename')
