from django.db import models
import uuid

class IPCheck(models.Model):
    ipcheck_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=255)
    update_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'ip_check'  
        managed = False  

    def __str__(self):
        return str(self.ipcheck_id)
    

class MNCMCCCheck(models.Model):
    senderidcheck_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=255)
    update_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'mnc_mcc_check'  # This specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return str(self.senderidcheck_id)



class InvoiceType(models.Model):
    invoicetype_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    invoicetype = models.CharField(max_length=255)
    update_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'invoicetype'  # This specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return str(self.invoicetype_id)


class Protocol(models.Model):
    senderidcheck_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=255)
    update_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'protocol'  # This specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return str(self.senderidcheck_id)
    


class RouteCheck(models.Model):
    routecheck_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=255)
    update_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'route_check'  # This specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return str(self.routecheck_id)
    

class RouteType(models.Model):
    routetype_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=255)
    update_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'route_type'  # This specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return str(self.routetype_id)


class SenderIdCheck(models.Model):
    senderidcheck_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=255)
    update_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'senderid_check'  # This specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return str(self.senderidcheck_id)


class SmsType(models.Model):
    smstype_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    smstype = models.CharField(max_length=255)
    update_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'smstype'  # This specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return str(self.smstype_id)
    


class Status(models.Model):
    senderidcheck_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=255)
    update_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'status'  # This specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return str(self.senderidcheck_id)



class PriceCheck(models.Model):
    pricecheck_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=255)
    update_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'price_check'  # This specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return str(self.pricecheck_id)



from django.db import models

class SmsServiceProvider(models.Model):
    smsserviceprovidername = models.CharField(max_length=255, primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'smsserviceprovide'  # Maps the model to the specified table
        managed = False  # Prevents Django from managing the table schema

    def __str__(self):
        return self.smsserviceprovidername

