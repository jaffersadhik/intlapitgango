from django.db import models
import uuid
class PriceAccount(models.Model):
    price_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #cost id name 
    created_date = models.DateTimeField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)  # Maps to double in MySQL
    update_date = models.DateTimeField(null=True, blank=True)
    accountname = models.CharField(max_length=16)
    dial_in_code = models.BigIntegerField()

    class Meta:
        db_table = 'price_account'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return self.ipaccount_id


class PriceAccountInvoiceDate(models.Model):
    price_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #cost id name 
    created_date = models.DateTimeField(null=True, blank=True)
    invoice_date = models.BigIntegerField(null=True, blank=True)  # Maps to bigint in MySQL
    price = models.FloatField(null=True, blank=True)  # Maps to double in MySQL
    update_date = models.DateTimeField(null=True, blank=True)
    accountname = models.CharField(max_length=16)
    dial_in_code = models.BigIntegerField()

    class Meta:
        db_table = 'price_account_invoicedate'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return self.ipaccount_id


class PriceAccountMncmcc(models.Model):
    price_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #cost id name 
    created_date = models.DateTimeField(null=True, blank=True)
    mcc = models.BigIntegerField(null=True, blank=True)  # Maps to bigint in MySQL
    mnc = models.BigIntegerField(null=True, blank=True)  # Maps to bigint in MySQL
    price = models.FloatField(null=True, blank=True)  # Maps to double in MySQL
    update_date = models.DateTimeField(null=True, blank=True)
    accountname = models.CharField(max_length=16)
    dial_in_code = models.BigIntegerField()

    class Meta:
        db_table = 'price_account_mncmcc'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return self.price_id


class PriceAccountMncmccInvoiceDate(models.Model):
    price_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #cost id name 
    created_date = models.DateTimeField(null=True, blank=True)
    invoice_date = models.BigIntegerField(null=True, blank=True)  # Maps to bigint in MySQL
    mcc = models.BigIntegerField(null=True, blank=True)  # Maps to bigint in MySQL
    mnc = models.BigIntegerField(null=True, blank=True)  # Maps to bigint in MySQL
    price = models.FloatField(null=True, blank=True)  # Maps to double in MySQL
    update_date = models.DateTimeField(null=True, blank=True)
    accountname = models.CharField(max_length=16)
    dial_in_code = models.BigIntegerField()

    class Meta:
        db_table = 'price_account_mncmcc_invoicedate'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return self.price_id


class PriceCustomer(models.Model):
    price_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #cost id name 
    created_date = models.DateTimeField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)  # Maps to double in MySQL
    update_date = models.DateTimeField(null=True, blank=True)
    dial_in_code = models.BigIntegerField()
    customername = models.CharField(max_length=16)

    class Meta:
        db_table = 'price_customer'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return self.price_id


class PriceCustomerInvoiceDate(models.Model):
    price_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #cost id name 
    created_date = models.DateTimeField(null=True, blank=True)
    invoice_date = models.BigIntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)  # Maps to double in MySQL
    update_date = models.DateTimeField(null=True, blank=True)
    dial_in_code = models.BigIntegerField()
    customername = models.CharField(max_length=16)

    class Meta:
        db_table = 'price_customer_invoicedate'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return self.price_id


class PriceCustomerMncmcc(models.Model):
    price_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #cost id name 
    created_date = models.DateTimeField(null=True, blank=True)
    mcc = models.BigIntegerField(null=True, blank=True)
    mnc = models.BigIntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)  # Maps to double in MySQL
    update_date = models.DateTimeField(null=True, blank=True)
    dial_in_code = models.BigIntegerField()
    customername = models.CharField(max_length=16)

    class Meta:
        db_table = 'price_customer_mncmcc'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return self.price_id


class PriceCustomerMncmccInvoiceDate(models.Model):
    price_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #cost id name 
    created_date = models.DateTimeField(null=True, blank=True)
    invoice_date = models.BigIntegerField(null=True, blank=True)
    mcc = models.BigIntegerField(null=True, blank=True)
    mnc = models.BigIntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)  # Maps to double in MySQL
    update_date = models.DateTimeField(null=True, blank=True)
    dial_in_code = models.BigIntegerField()
    customername = models.CharField(max_length=16)

    class Meta:
        db_table = 'price_customer_mncmcc_invoicedate'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return self.price_id


class PriceShared(models.Model):
    price_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #cost id name 
    created_date = models.DateTimeField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)  # Maps to double in MySQL
    update_date = models.DateTimeField(null=True, blank=True)
    dial_in_code = models.BigIntegerField()

    class Meta:
        db_table = 'price_shared'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return self.price_id
    
class PriceSharedInvoiceDate(models.Model):
    price_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #cost id name 
    created_date = models.DateTimeField(null=True, blank=True)
    invoice_date = models.BigIntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)  # Maps to double in MySQL
    update_date = models.DateTimeField(null=True, blank=True)
    dial_in_code = models.BigIntegerField()

    class Meta:
        db_table = 'price_shared_invoicedate'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return self.price_id


class PriceSharedMncmcc(models.Model):
    price_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #cost id name 
    created_date = models.DateTimeField(null=True, blank=True)
    mcc = models.BigIntegerField(null=True, blank=True)
    mnc = models.BigIntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)  # Maps to double in MySQL
    update_date = models.DateTimeField(null=True, blank=True)
    dial_in_code = models.BigIntegerField()

    class Meta:
        db_table = 'price_shared_mncmcc'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return self.price_id



class PriceSharedMncmccInvoiceDate(models.Model):
    price_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #cost id name 
    created_date = models.DateTimeField(null=True, blank=True)
    invoice_date = models.BigIntegerField(null=True, blank=True)
    mcc = models.BigIntegerField(null=True, blank=True)
    mnc = models.BigIntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)  # Maps to double in MySQL
    update_date = models.DateTimeField(null=True, blank=True)
    dial_in_code = models.BigIntegerField()

    class Meta:
        db_table = 'price_shared_mncmcc_invoicedate'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return self.price_id
