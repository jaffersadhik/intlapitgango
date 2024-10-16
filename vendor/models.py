from django.db import models
import uuid
class Carrier(models.Model):
    # Remove the carrier_id field and set carriername as the primary key
    carriername = models.CharField(max_length=16, primary_key=True)  # Set carriername as primary key
    companyname = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'carrier'  # This specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return self.carriername  # Return the carriername for string representation


class SMSC(models.Model):
    # carrier_id = models.CharField(max_length=255)  # Changed to carrier_id
    created_date = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    mode = models.CharField(max_length=255)
    password = models.CharField(max_length=9, blank=True, null=True)
    port = models.BigIntegerField(blank=True, null=True)
    securelevel = models.CharField(max_length=255)
    smscid = models.CharField(max_length=10,primary_key=True)  # Set smscid as the primary key
    tps = models.BigIntegerField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    username = models.CharField(max_length=16, blank=True, null=True)
    carriername = models.CharField(max_length=255)
    dial_in_code = models.BigIntegerField()  # Changed from country_code_iso3 to dial_in_code
    currencycode = models.CharField(max_length=255)
    routetype = models.CharField(max_length=255)
    smstype = models.CharField(max_length=255)
    timezone_id = models.CharField(max_length=255)

    class Meta:
        db_table = 'smsc'  # Explicitly specify the table name in MySQL
        managed = False  # This prevents Django from managing the table

    def __str__(self):
        return self.smsgcid  # Return smscid as it is the primary key

