from django.db import models
import uuid
class IpAccount(models.Model):
    ipaccount_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    accountname = models.CharField(max_length=16)

    class Meta:
        db_table = 'ip_account'  # This specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return str(self.ipaccount_id)


class IpCustomer(models.Model):
    ipcustomer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    customername = models.CharField(max_length=16)

    class Meta:
        db_table = 'ip_customer'  # This specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return str(self.ipcustomer_id)


class IpShared(models.Model):
    ip_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'ip_shared'  # This specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return str(self.ip_id)
