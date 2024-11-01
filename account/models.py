from django.db import models
from django.core.exceptions import PermissionDenied
from django.dispatch import receiver
from django.db.models.signals import pre_delete
import uuid

class Account(models.Model):
    account_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(blank=True, null=True)
    emailstatus = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    loginpassword = models.CharField(max_length=9, blank=True, null=True)
    mobilestatus = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=9, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    username = models.CharField(max_length=16, blank=True, null=True)
    dial_in_code = models.BigIntegerField()
    currencycode = models.CharField(max_length=255)
    customer_id = models.CharField(max_length=255)
    ipcheck = models.CharField(max_length=255)
    mncmcccheck = models.CharField(max_length=255)
    pricecheck = models.CharField(max_length=255)
    protocol = models.CharField(max_length=255)
    routecheck = models.CharField(max_length=255)
    routetype = models.CharField(max_length=255)
    senderidcheck = models.CharField(max_length=255)
    smstype = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    timezone_id = models.CharField(max_length=255)
    errorcode_type = models.CharField(max_length=255, blank=True, null=True)  # New field added
    cluster = models.CharField(max_length=255, blank=True, null=True)  # New field added

    class Meta:
        db_table = 'account'  # This specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return str(self.account_id)



class Company(models.Model):
    company_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    activestatus = models.BooleanField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    blockcustomer = models.BooleanField(null=True, blank=True)
    create_date = models.DateTimeField(null=True, blank=True)
    createduser_id = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    emailverified = models.BooleanField(null=True, blank=True)
    fullname = models.CharField(max_length=100, null=True, blank=True)
    mobilenumber = models.BigIntegerField(null=True, blank=True)
    mobilenumberverified = models.BooleanField(null=True, blank=True)
    password = models.CharField(max_length=9, null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    username = models.CharField(max_length=16, null=True, blank=True)

    def __str__(self):
        return str(self.fullname) or str(self.company_id)

    class Meta:
        db_table = 'company'  



class Customer(models.Model):
    customer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    companyname = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    customername = models.CharField(max_length=16, blank=True, null=True)
    email = models.CharField(max_length=255)
    emailstatus = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    loginpassword = models.CharField(max_length=9, blank=True, null=True)
    mobile = models.BigIntegerField()
    mobilestatus = models.CharField(max_length=255, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    invoicetype = models.CharField(max_length=255)

    class Meta:
        db_table = 'customer'  # This specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return str(self.customer_id)

@receiver(pre_delete)
def log_update_changes(sender, instance, **kwargs):
    raise PermissionDenied(f"Deletion is not allowed for {sender._meta.model_name}.")



