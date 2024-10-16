from django.db import models
import uuid

class Route(models.Model):
    route_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    routename = models.CharField(max_length=16, null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(null=True, blank=True)
# createda
    class Meta:
        db_table = 'route'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return self.route_id
    

from django.db import models

class RouteAccount(models.Model):
    routemapping_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    weight = models.SmallIntegerField(null=True, blank=True)
    accountname = models.CharField(max_length=16)
    dial_in_code = models.BigIntegerField()
    routename = models.CharField(max_length=16)
    smscid = models.CharField(max_length=10)

    class Meta:
        db_table = 'route_account'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return self.routemapping_id
    
from django.db import models

class RouteAccountMncmcc(models.Model):
    routemapping_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(null=True, blank=True)
    mcc = models.BigIntegerField(null=True, blank=True)
    mnc = models.BigIntegerField(null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    weight = models.SmallIntegerField(null=True, blank=True)
    accountname = models.CharField(max_length=16)
    dial_in_code = models.BigIntegerField()
    routename = models.CharField(max_length=16)
    smscid = models.CharField(max_length=10)

    class Meta:
        db_table = 'route_account_mncmcc'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return self.routemapping_id

class RouteCustomer(models.Model):
    routemapping_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    weight = models.SmallIntegerField(null=True, blank=True)
    dial_in_code = models.BigIntegerField()
    customername = models.CharField(max_length=16)
    routename = models.CharField(max_length=16)
    smscid = models.CharField(max_length=10)

    class Meta:
        db_table = 'route_customer'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return self.routemapping_id
    

class RouteCustomerMncMcc(models.Model):
    routemapping_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(null=True, blank=True)
    mcc = models.BigIntegerField(null=True, blank=True)
    mnc = models.BigIntegerField(null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    weight = models.SmallIntegerField(null=True, blank=True)
    dial_in_code = models.BigIntegerField()
    customername = models.CharField(max_length=16)
    routename = models.CharField(max_length=16)
    smscid = models.CharField(max_length=10)

    class Meta:
        db_table = 'route_customer_mncmcc'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return self.routemapping_id

from django.db import models

class RouteShared(models.Model):
    routemapping_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    weight = models.SmallIntegerField(null=True, blank=True)
    dial_in_code = models.BigIntegerField()
    routename = models.CharField(max_length=16)
    smscid = models.CharField(max_length=10)

    class Meta:
        db_table = 'route_shared'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return self.routemapping_id

from django.db import models

class RouteSharedMncmcc(models.Model):
    routemapping_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(null=True, blank=True)
    mcc = models.BigIntegerField(null=True, blank=True)
    mnc = models.BigIntegerField(null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    weight = models.SmallIntegerField(null=True, blank=True)
    dial_in_code = models.BigIntegerField()
    routename = models.CharField(max_length=16)
    smscid = models.CharField(max_length=10)

    class Meta:
        db_table = 'route_shared_mncmcc'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return self.routemapping_id
