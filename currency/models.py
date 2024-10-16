from django.db import models
import uuid

class Currency(models.Model):
    currency_id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(blank=True, null=True)
    currencycode = models.CharField(max_length=9, blank=True, null=True)
    currencyname = models.CharField(max_length=100, blank=True, null=True)
    territory = models.CharField(max_length=255, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'currency'  # This specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return str(self.currency_id)


class CurrencyConversion(models.Model):
    currencyconversion_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    conversionrate = models.FloatField()
    created_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    from_currency = models.CharField(max_length=9)
    to_currency = models.CharField(max_length=9)

    class Meta:
        db_table = 'currency_conversion'  # This specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return str(self.currencyconversion_id)

class CurrencyConversionInvoiceDate(models.Model):
    currencyconversion_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    conversionrate = models.FloatField()
    created_date = models.DateTimeField(blank=True, null=True)
    invoice_date = models.BigIntegerField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    from_currency = models.CharField(max_length=9)
    to_currency = models.CharField(max_length=9)

    class Meta:
        db_table = 'currency_conversion_invoicedate'  # This specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return str(self.currencyconversion_id)