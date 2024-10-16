from django.db import models
import uuid



class ErrorcodeAccount(models.Model):
    errorcode_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    errorcode = models.CharField(max_length=255, null=True, blank=True)
    platformerrorcode = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    accountname = models.CharField(max_length=255)

    class Meta:
        db_table = 'errorcode_account'  # Maps the model to the existing MySQL table
        managed = False  # Prevents Django from creating/modifying this table

    def __str__(self):
        return str(self.errorcode_id)

class ErrorcodeCarrier(models.Model):
    errorcode_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    errorcode = models.CharField(max_length=255, null=True, blank=True)
    platformerrorcode = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    carriername  = models.CharField(max_length=255)

    class Meta:
        db_table = 'errorcode_carrier'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return self.errorcode_id

from django.db import models

class ErrorcodePlatform(models.Model):
    errorcode_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    errorcode = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'errorcode_platform'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return self.errorcode_id


class ErrorcodeCustomer(models.Model):
    errorcode_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    errorcode = models.CharField(max_length=255, null=True, blank=True)
    platformerrorcode = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    customername = models.CharField(max_length=255)

    class Meta:
        db_table = 'errorcode_customer'  # Maps the model to the existing MySQL table
        managed = False  # Prevents Django from creating/modifying this table

    def __str__(self):
        return str(self.errorcode_id)
    

class ErrorcodeSmsServiceProvider(models.Model):
    errorcode_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    errorcode = models.CharField(max_length=255, null=True, blank=True)
    platformerrorcode = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    smsserviceprovider = models.CharField(max_length=255)

    class Meta:
        db_table = 'errorcode_smsserviceprovider'  # Maps the model to the newly created table
        managed = False  # Prevents Django from modifying the table

    def __str__(self):
        return str(self.errorcode_id)