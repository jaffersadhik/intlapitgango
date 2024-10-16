from django.db import models
import uuid
class WebhookAccount(models.Model):
    webhookaccount_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(null=True, blank=True)
    date_format = models.CharField(max_length=255, null=True, blank=True)
    postdata = models.CharField(max_length=255, null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    weghookurl = models.CharField(max_length=255, null=True, blank=True)
    accountname = models.CharField(max_length=16)

    class Meta:
        db_table = 'webhook_account'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return self.webhookaccount_id



class WebhookCustomer(models.Model):
    webhookcustomer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(null=True, blank=True)
    date_format = models.CharField(max_length=255, null=True, blank=True)
    postdata = models.CharField(max_length=255, null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    weghookurl = models.CharField(max_length=255, null=True, blank=True)
    customername = models.CharField(max_length=16)

    class Meta:
        db_table = 'webhook_customer'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return self.webhookcustomer_id


class WebhookParameterIndex(models.Model):
    webhookparameter_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(null=True, blank=True)
    indexnumber = models.SmallIntegerField(null=True, blank=True)
    parametername = models.CharField(max_length=255, null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'webhook_parameter_index'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return self.webhookaccount_id
