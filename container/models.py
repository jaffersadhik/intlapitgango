from django.db import models

class ContainerBillingLog(models.Model):
    billinglog_id = models.CharField(max_length=255, primary_key=True)
    billinglogname = models.CharField(max_length=100, null=True, blank=True)
    created_date = models.DateTimeField(null=True, blank=True)
    deploystatus = models.BooleanField(null=True, blank=True)  # bit(1) in MySQL maps to BooleanField in Django
    runningstatus = models.BooleanField(null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    gatewayip_id = models.CharField(max_length=255)
    gatewayport_id = models.CharField(max_length=255)
    mysqlbillingdb_id = models.CharField(max_length=255)

    class Meta:
        db_table = 'container_billinglog'  # Specifies the exact MySQL table name
        managed = False  # Prevents Django from creating or modifying the table

    def __str__(self):
        return self.billinglog_id


class ContainerConcateReceiver(models.Model):
    concatereceiver_id = models.CharField(max_length=255, primary_key=True)
    concatereceivername = models.CharField(max_length=100, null=True, blank=True)
    created_date = models.DateTimeField(null=True, blank=True)
    deploymentstatus = models.BooleanField(null=True, blank=True)  # bit(1) -> BooleanField in Django
    runningstatus = models.BooleanField(null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    gatewayip_id = models.CharField(max_length=255)
    gatewayport_id = models.CharField(max_length=255)

    class Meta:
        db_table = 'container_concatereceiver'  # Specifies the MySQL table name
        managed = False  # Django will not create or modify the table

    def __str__(self):
        return self.concatereceiver_id



class ContainerDNReceiver(models.Model):
    dnreceiver_id = models.CharField(max_length=255, primary_key=True)
    created_date = models.DateTimeField(null=True, blank=True)
    deploymentstatus = models.BooleanField(null=True, blank=True)  # Maps to bit(1) in MySQL
    dnreceivername = models.CharField(max_length=100, null=True, blank=True)
    runningstatus = models.BooleanField(null=True, blank=True)  # Maps to bit(1) in MySQL
    update_date = models.DateTimeField(null=True, blank=True)
    gatewayip_id = models.CharField(max_length=255)
    gatewayport_id = models.CharField(max_length=255)

    class Meta:
        db_table = 'container_dnreceiver'  # Specifies the MySQL table name
        managed = False  # Django will not create or modify the table

    def __str__(self):
        return self.dnreceiver_id
    
class ContainerHttpInterface(models.Model):
    httpinterface_id = models.CharField(max_length=255, primary_key=True)
    created_date = models.DateTimeField(null=True, blank=True)
    deploymentstatus = models.BooleanField(null=True, blank=True)  # Maps to bit(1) in MySQL
    httpinterfacename = models.CharField(max_length=100, null=True, blank=True)
    runningstatus = models.BooleanField(null=True, blank=True)  # Maps to bit(1) in MySQL
    update_date = models.DateTimeField(null=True, blank=True)
    gatewayip_id = models.CharField(max_length=255)
    gatewayport_id = models.CharField(max_length=255)

    class Meta:
        db_table = 'container_httpinterface'  # Specifies the MySQL table name
        managed = False  # Django will not create or modify the table

    def __str__(self):
        return self.httpinterface_id

class ContainerHttpLoadBalancer(models.Model):
    httploadbalancer_id = models.CharField(max_length=255, primary_key=True)
    created_date = models.DateTimeField(null=True, blank=True)
    deploymentstatus = models.BooleanField(null=True, blank=True)  # Maps to bit(1) in MySQL
    httploadbalancername = models.CharField(max_length=100, null=True, blank=True)
    runningstatus = models.BooleanField(null=True, blank=True)  # Maps to bit(1)
    update_date = models.DateTimeField(null=True, blank=True)
    gatewayip_id = models.CharField(max_length=255)
    gatewayport_id = models.CharField(max_length=255)

    class Meta:
        db_table = 'container_httploadbalancer'  # Specifies the exact MySQL table name
        managed = False  # Django won't create or modify the table

    def __str__(self):
        return self.httploadbalancer_id
    
class ContainerIP(models.Model):
    gatewayip_id = models.CharField(max_length=255, primary_key=True)
    serverip = models.CharField(max_length=255, null=True, blank=True)
    servername = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'container_ip'  # Specifies the exact MySQL table name
        managed = False  # Django won't create or modify the table

    def __str__(self):
        return self.gatewayip_id
    
class ContainerKannel(models.Model):
    kannel_id = models.CharField(max_length=255, primary_key=True)
    created_date = models.DateTimeField(null=True, blank=True)
    dnacceptancestatus = models.CharField(max_length=255, null=True, blank=True)
    kannelname = models.CharField(max_length=100, null=True, blank=True)
    sendsmspassword = models.CharField(max_length=255, null=True, blank=True)
    sendsmsusername = models.CharField(max_length=255, null=True, blank=True)
    smsacceptancestatus = models.CharField(max_length=255, null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    gatewayip_id = models.CharField(max_length=255)
    gatewayport_id = models.CharField(max_length=255)

    class Meta:
        db_table = 'container_kannel'  # Specifies the exact MySQL table name
        managed = False  # Django won't create or modify the table

    def __str__(self):
        return self.kannel_id
    
class ContainerMySQLBillingDB(models.Model):
    mysqlbillingdb_id = models.CharField(max_length=255, primary_key=True)
    created_date = models.DateTimeField(null=True, blank=True)
    deploymentstatus = models.BooleanField(null=True, blank=True)
    mysqlbillingdbname = models.CharField(max_length=100, null=True, blank=True)
    runningstatus = models.BooleanField(null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    gatewayip_id = models.CharField(max_length=255)
    gatewayport_id = models.CharField(max_length=255)

    class Meta:
        db_table = 'container_mysqlbillingdb'  # Specifies the exact MySQL table name
        managed = False  # Django won't create or modify the table

    def __str__(self):
        return self.mysqlbillingdb_id
    
class ContainerMySQLQueueDB(models.Model):
    mysqlqueuedb_id = models.CharField(max_length=255, primary_key=True)
    created_date = models.DateTimeField(null=True, blank=True)
    deploymentstatus = models.BooleanField(null=True, blank=True)
    mysqlqueuedbname = models.CharField(max_length=100, null=True, blank=True)
    runningstatus = models.BooleanField(null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    gatewayip_id = models.CharField(max_length=255)
    gatewayport_id = models.CharField(max_length=255)

    class Meta:
        db_table = 'container_mysqlqueuedb'  # Specifies the exact MySQL table name
        managed = False  # Django won't create or modify the table

    def __str__(self):
        return self.mysqlqueuedb_id
    

class ContainerPort(models.Model):
    containerport_id = models.CharField(max_length=255, primary_key=True)
    bearerboxport = models.BigIntegerField(null=True, blank=True)
    concatereceiverport = models.BigIntegerField(null=True, blank=True)
    created_date = models.DateTimeField(null=True, blank=True)
    dnloadbalancerport = models.BigIntegerField(null=True, blank=True)
    dnlogport = models.BigIntegerField(null=True, blank=True)
    dnpostlogport = models.BigIntegerField(null=True, blank=True)
    dnreceiverport = models.BigIntegerField(null=True, blank=True)
    dockerregistryport = models.BigIntegerField(null=True, blank=True)
    httpinterfaceport = models.BigIntegerField(null=True, blank=True)
    httploadbalancerport = models.BigIntegerField(null=True, blank=True)
    kannelstatusport = models.BigIntegerField(null=True, blank=True)
    mysqlbillingdbport = models.BigIntegerField(null=True, blank=True)
    mysqlconcatedbport = models.BigIntegerField(null=True, blank=True)
    mysqlkanneldbport = models.BigIntegerField(null=True, blank=True)
    mysqlqueuedbport = models.BigIntegerField(null=True, blank=True)
    portname = models.CharField(max_length=50, null=True, blank=True)
    redisqueuedbport = models.BigIntegerField(null=True, blank=True)
    requestprocessorport = models.BigIntegerField(null=True, blank=True)
    requestreceiverport = models.BigIntegerField(null=True, blank=True)
    sendsmsport = models.BigIntegerField(null=True, blank=True)
    smppinterfaceport = models.BigIntegerField(null=True, blank=True)
    smpploadbalancerport = models.BigIntegerField(null=True, blank=True)
    smslogport = models.BigIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'container_port'  # Specifies the exact MySQL table name
        managed = False  # Django won't create or modify the table

    def __str__(self):
        return self.containerport_id



class ContainerRedisQueueDB(models.Model):
    redisqueuedb_id = models.CharField(max_length=255, primary_key=True)
    created_date = models.DateTimeField(null=True, blank=True)
    deploymentstatus = models.BinaryField(null=True, blank=True)  # Bit(1) stored as binary
    redisqueuedbname = models.CharField(max_length=100, null=True, blank=True)
    runningstatus = models.BinaryField(null=True, blank=True)  # Bit(1) stored as binary
    update_date = models.DateTimeField(null=True, blank=True)
    gatewayip_id = models.CharField(max_length=255)
    gatewayport_id = models.CharField(max_length=255)

    class Meta:
        db_table = 'container_redisqueuedb'  # Specifies the exact MySQL table name
        managed = False  # Django won't create or modify the table

    def __str__(self):
        return self.redisqueuedb_id
    

class ContainerRequestProcessor(models.Model):
    requestprocessor_id = models.CharField(max_length=255, primary_key=True)
    created_date = models.DateTimeField(null=True, blank=True)
    deploymentstatus = models.BinaryField(null=True, blank=True)  # Bit(1) stored as binary
    requestprocessorname = models.CharField(max_length=100, null=True, blank=True)
    runningstatus = models.BinaryField(null=True, blank=True)  # Bit(1) stored as binary
    update_date = models.DateTimeField(null=True, blank=True)
    redisqueuedb_id = models.CharField(max_length=255)
    gatewayip_id = models.CharField(max_length=255)
    gatewayport_id = models.CharField(max_length=255)

    class Meta:
        db_table = 'container_requestprocessor'  # Specifies the exact MySQL table name
        managed = False  # Django won't create or modify the table

    def __str__(self):
        return self.requestprocessor_id

class ContainerSMPPInterface(models.Model):
    smppinterface_id = models.CharField(max_length=255, primary_key=True)
    created_date = models.DateTimeField(null=True, blank=True)
    deploymentstatus = models.BinaryField(null=True, blank=True)  # Bit(1) stored as binary
    runningstatus = models.BinaryField(null=True, blank=True)  # Bit(1) stored as binary
    smppinterfacename = models.CharField(max_length=100, null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    gatewayip_id = models.CharField(max_length=255)
    gatewayport_id = models.CharField(max_length=255)

    class Meta:
        db_table = 'container_smppinterface'  # Specifies the exact MySQL table name
        managed = False  # Django won't create or modify the table

    def __str__(self):
        return self.smppinterface_id
    
class ContainerSMPPLoadBalancer(models.Model):
    smpploadbalancer_id = models.CharField(max_length=255, primary_key=True)
    created_date = models.DateTimeField(null=True, blank=True)
    deploymentstatus = models.BinaryField(null=True, blank=True)  # Bit(1) stored as binary
    runningstatus = models.BinaryField(null=True, blank=True)  # Bit(1) stored as binary
    smpploadbalancername = models.CharField(max_length=100, null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    gatewayip_id = models.CharField(max_length=255)
    gatewayport_id = models.CharField(max_length=255)

    class Meta:
        db_table = 'container_smpploadbalancer'  # Specifies the exact MySQL table name
        managed = False  # Django won't create or modify the table

    def __str__(self):
        return self.smpploadbalancer_id
    
class ContainerTLVTag(models.Model):
    dlvtag_id = models.CharField(max_length=255, primary_key=True)
    created_date = models.DateTimeField(null=True, blank=True)
    length = models.BigIntegerField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    tag = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'container_tlvtag'  # Specifies the exact MySQL table name
        managed = False  # Django won't create or modify the table

    def __str__(self):
        return self.dlvtag_id