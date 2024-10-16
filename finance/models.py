from django.db import models
import uuid

class Payment(models.Model):
    payment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.FloatField(null=True, blank=True)
    currency = models.CharField(max_length=255, null=True, blank=True)
    payer_email = models.EmailField(max_length=255, null=True, blank=True)
    payment_date = models.DateTimeField(null=True, blank=True)
    payment_method = models.CharField(max_length=255, null=True, blank=True)
    payment_status = models.CharField(max_length=255, null=True, blank=True)
    transaction_id = models.CharField(max_length=255, null=True, blank=True)
    customername = models.CharField(max_length=255)

    class Meta:
        db_table = 'payment'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return str(self.payment_id)


class Invoice(models.Model):
    invoice_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(null=True, blank=True)
    invoice_date = models.BigIntegerField(null=True, blank=True)
    invoice_period_end_date = models.BigIntegerField(null=True, blank=True)
    invoice_period_start_date = models.BigIntegerField(null=True, blank=True)
    invoiceamount = models.FloatField(null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    accountname = models.CharField(max_length=16)

    class Meta:
        db_table = 'invoice' # Specifies the exact MySQL table name
        managed = False # Prevents Django from creating or modifying the table

    def __str__(self):
        return self.invoice_id



class Outstanding(models.Model):
    outstanding_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(null=True, blank=True)
    invoice_amount = models.FloatField(null=True, blank=True)
    invoice_period_year = models.BigIntegerField(null=True, blank=True)
    outstanding_period_year = models.BigIntegerField(null=True, blank=True)
    outstandingamount = models.FloatField(null=True, blank=True)
    payment_amount = models.FloatField(null=True, blank=True)
    payment_period_year = models.BigIntegerField(null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    customername = models.CharField(max_length=255)

    class Meta:
        db_table = 'outstanding'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return self.outstanding_id
