from django.db import models
import uuid

class Country(models.Model):
    country_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country = models.CharField(max_length=255, blank=True, null=True)
    country_code_iso2 = models.CharField(max_length=255, blank=True, null=True)
    country_code_iso3 = models.CharField(max_length=255, blank=True, null=True)
    country_code_iso_numeric = models.BigIntegerField(blank=True, null=True)
    country_short_name = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    dial_in_code = models.BigIntegerField(blank=True, null=True)
    dial_in_code_full = models.BigIntegerField(blank=True, null=True)
    max_mobile_length = models.BigIntegerField(blank=True, null=True)
    min_mobile_length = models.BigIntegerField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'country'  # This specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return str(self.country_id)  # Convert UUID to string



class MncMcc(models.Model):
    mncmcc_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(blank=True, null=True)
    mcc = models.BigIntegerField(blank=True, null=True)
    mnc = models.BigIntegerField(blank=True, null=True)
    networkoperatorname = models.CharField(max_length=255, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    dial_in_code = models.BigIntegerField()

    class Meta:
        db_table = 'mnc_mcc'  # This specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return str(self.mncmcc_id)



class MncMccPrefix(models.Model):
    mccmncprefix_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    countrycode = models.BigIntegerField(blank=True, null=True)
    mcc = models.BigIntegerField(blank=True, null=True)
    mnc = models.BigIntegerField(blank=True, null=True)
    prefix = models.BigIntegerField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'mnc_mcc_prefix'  # This specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return str(self.mccmncprefix_id)


class WorldTimezone(models.Model):
    timezone_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(blank=True, null=True)
    displayname = models.CharField(max_length=255, blank=True, null=True)
    longname = models.CharField(max_length=255, blank=True, null=True)
    offset = models.CharField(max_length=255, blank=True, null=True)
    shortname = models.CharField(max_length=255, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    zonename = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'worldtimezone'  # This specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return str(self.timezone_id)
