from django.db import models
import uuid

class SenderIdAccount(models.Model):
    accountsenderid_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(blank=True, null=True)
    senderid = models.CharField(max_length=255, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    accountname = models.CharField(max_length=16)

    class Meta:
        db_table = 'senderid_account'  # This specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return self.accountsenderid_id

class SenderIdCustomer(models.Model):
    customersenderid_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(blank=True, null=True)
    senderid = models.CharField(max_length=255, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    customername = models.CharField(max_length=16)

    class Meta:
        db_table = 'senderid_customer'  # This specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return self.customersenderid_id
    

class SenderIdShared(models.Model):
    senderid_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(blank=True, null=True)
    senderid = models.CharField(max_length=255, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'senderid_shared'  # This specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return self.senderid_id
