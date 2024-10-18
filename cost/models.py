from django.db import models
import uuid

class CostCarrier(models.Model):
    cost_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #cost id name 
    cost = models.FloatField(null=True, blank=True)  # Maps to double in MySQL
    created_date = models.DateTimeField(null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    carriername = models.CharField(max_length=16)
    dial_in_code = models.BigIntegerField()

    class Meta:
        db_table = 'cost_carrier'  # This specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return str(self.cost_id)



class CostCarrierInvoiceDate(models.Model):
    cost_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #cost id name 
    cost = models.FloatField(null=True, blank=True)  # Maps to double in MySQL
    created_date = models.DateTimeField(null=True, blank=True)
    invoice_date = models.BigIntegerField(null=True, blank=True)  # Maps to bigint in MySQL
    update_date = models.DateTimeField(null=True, blank=True)
    carriername = models.CharField(max_length=16)
    dial_in_code = models.BigIntegerField()

    class Meta:
        db_table = 'cost_carrier_invoicedate'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return str(self.cost_id)



class CostCarrierMncmcc(models.Model): 
    cost_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cost = models.FloatField(null=True, blank=True)  # Maps to double in MySQL
    created_date = models.DateTimeField(null=True, blank=True)
    mcc = models.BigIntegerField(null=True, blank=True)  # Maps to bigint in MySQL
    mnc = models.BigIntegerField(null=True, blank=True)  # Maps to bigint in MySQL
    update_date = models.DateTimeField(null=True, blank=True)
    carriername = models.CharField(max_length=16)
    dial_in_code = models.BigIntegerField()

    class Meta:
        db_table = 'cost_carrier_mncmcc'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return str(self.cost_id)



class CostCarrierMncmccInvoiceDate(models.Model):
    cost_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cost = models.FloatField(null=True, blank=True)  # Maps to double in MySQL
    created_date = models.DateTimeField(null=True, blank=True)
    invoice_date = models.BigIntegerField(null=True, blank=True)  # Maps to bigint in MySQL
    mcc = models.BigIntegerField(null=True, blank=True)  # Maps to bigint in MySQL
    mnc = models.BigIntegerField(null=True, blank=True)  # Maps to bigint in MySQL
    update_date = models.DateTimeField(null=True, blank=True)
    carriername = models.CharField(max_length=16)
    dial_in_code = models.BigIntegerField()

    class Meta:
        db_table = 'cost_carrier_mncmcc_invoicedate'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return str(self.cost_id)



class CostSMSC(models.Model):
    cost_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cost = models.FloatField(null=True, blank=True)  # Maps to double in MySQL
    created_date = models.DateTimeField(null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    dial_in_code = models.BigIntegerField()
    smscid = models.CharField(max_length=255)

    class Meta:
        db_table = 'cost_smsc'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return str(self.cost_id)



class CostSMSCInvoiceDate(models.Model):
    cost_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cost = models.FloatField(null=True, blank=True)  # Maps to double in MySQL
    created_date = models.DateTimeField(null=True, blank=True)
    invoice_date = models.BigIntegerField(null=True, blank=True)  # Maps to bigint in MySQL
    update_date = models.DateTimeField(null=True, blank=True)
    dial_in_code = models.BigIntegerField()
    smscid = models.CharField(max_length=255)

    class Meta:
        db_table = 'cost_smsc_invoicedate'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return str(self.cost_id)


class CostSMSCmncmcc(models.Model):
    cost_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cost = models.FloatField(null=True, blank=True)  # Maps to double in MySQL
    created_date = models.DateTimeField(null=True, blank=True)
    mcc = models.BigIntegerField(null=True, blank=True)  # Maps to bigint in MySQL
    mnc = models.BigIntegerField(null=True, blank=True)  # Maps to bigint in MySQL
    update_date = models.DateTimeField(null=True, blank=True)
    dial_in_code = models.BigIntegerField()
    smscid = models.CharField(max_length=255)

    class Meta:
        db_table = 'cost_smsc_mncmcc'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return str(self.cost_id)
    

class CostSMSCmncmccInvoiceDate(models.Model):
    cost_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cost = models.FloatField(null=True, blank=True)  # Maps to double in MySQL
    created_date = models.DateTimeField(null=True, blank=True)
    invoice_date = models.BigIntegerField(null=True, blank=True)  # Maps to bigint in MySQL
    mcc = models.BigIntegerField(null=True, blank=True)  # Maps to bigint in MySQL
    mnc = models.BigIntegerField(null=True, blank=True)  # Maps to bigint in MySQL
    update_date = models.DateTimeField(null=True, blank=True)
    dial_in_code = models.BigIntegerField()
    smscid = models.CharField(max_length=255)

    class Meta:
        db_table = 'cost_smsc_mncmcc_invoicedate'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return str(self.cost_id)

