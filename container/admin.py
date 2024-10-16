from django.contrib import admin
from .models import (
    ContainerBillingLog,
    ContainerConcateReceiver,
    ContainerDNReceiver,
    ContainerHttpInterface,
    ContainerHttpLoadBalancer,
    ContainerIP,
    ContainerKannel,
    ContainerMySQLBillingDB,
    ContainerMySQLQueueDB,
    ContainerPort,
    ContainerRedisQueueDB,
    ContainerRequestProcessor,
    ContainerSMPPInterface,
    ContainerSMPPLoadBalancer,
    ContainerTLVTag
)

@admin.register(ContainerBillingLog)
class ContainerBillingLogAdmin(admin.ModelAdmin):
    list_display = ('billinglog_id', 'billinglogname', 'created_date', 'deploystatus', 'runningstatus', 'update_date', 'gatewayip_id', 'gatewayport_id', 'mysqlbillingdb_id')
    search_fields = ('billinglog_id', 'billinglogname')

@admin.register(ContainerConcateReceiver)
class ContainerConcateReceiverAdmin(admin.ModelAdmin):
    list_display = ('concatereceiver_id', 'concatereceivername', 'created_date', 'deploymentstatus', 'runningstatus', 'update_date', 'gatewayip_id', 'gatewayport_id')
    search_fields = ('concatereceiver_id', 'concatereceivername')

@admin.register(ContainerDNReceiver)
class ContainerDNReceiverAdmin(admin.ModelAdmin):
    list_display = ('dnreceiver_id', 'created_date', 'deploymentstatus', 'dnreceivername', 'runningstatus', 'update_date', 'gatewayip_id', 'gatewayport_id')
    search_fields = ('dnreceiver_id', 'dnreceivername')

@admin.register(ContainerHttpInterface)
class ContainerHttpInterfaceAdmin(admin.ModelAdmin):
    list_display = ('httpinterface_id', 'created_date', 'deploymentstatus', 'httpinterfacename', 'runningstatus', 'update_date', 'gatewayip_id', 'gatewayport_id')
    search_fields = ('httpinterface_id', 'httpinterfacename')

@admin.register(ContainerHttpLoadBalancer)
class ContainerHttpLoadBalancerAdmin(admin.ModelAdmin):
    list_display = ('httploadbalancer_id', 'created_date', 'deploymentstatus', 'httploadbalancername', 'runningstatus', 'update_date', 'gatewayip_id', 'gatewayport_id')
    search_fields = ('httploadbalancer_id', 'httploadbalancername')

@admin.register(ContainerIP)
class ContainerIPAdmin(admin.ModelAdmin):
    list_display = ('gatewayip_id', 'serverip', 'servername')
    search_fields = ('gatewayip_id', 'serverip')

@admin.register(ContainerKannel)
class ContainerKannelAdmin(admin.ModelAdmin):
    list_display = ('kannel_id', 'created_date', 'dnacceptancestatus', 'kannelname', 'sendsmspassword', 'sendsmsusername', 'smsacceptancestatus', 'update_date', 'gatewayip_id', 'gatewayport_id')
    search_fields = ('kannel_id', 'kannelname')

@admin.register(ContainerMySQLBillingDB)
class ContainerMySQLBillingDBAdmin(admin.ModelAdmin):
    list_display = ('mysqlbillingdb_id', 'created_date', 'deploymentstatus', 'mysqlbillingdbname', 'runningstatus', 'update_date', 'gatewayip_id', 'gatewayport_id')
    search_fields = ('mysqlbillingdb_id', 'mysqlbillingdbname')

@admin.register(ContainerMySQLQueueDB)
class ContainerMySQLQueueDBAdmin(admin.ModelAdmin):
    list_display = ('mysqlqueuedb_id', 'created_date', 'deploymentstatus', 'mysqlqueuedbname', 'runningstatus', 'update_date', 'gatewayip_id', 'gatewayport_id')
    search_fields = ('mysqlqueuedb_id', 'mysqlqueuedbname')

@admin.register(ContainerPort)
class ContainerPortAdmin(admin.ModelAdmin):
    list_display = ('containerport_id', 'bearerboxport', 'concatereceiverport', 'created_date', 'dnloadbalancerport', 'dnlogport', 'dnpostlogport', 'dnreceiverport', 'dockerregistryport', 'httpinterfaceport', 'httploadbalancerport', 'kannelstatusport', 'mysqlbillingdbport', 'mysqlconcatedbport', 'mysqlkanneldbport', 'mysqlqueuedbport', 'portname', 'redisqueuedbport', 'requestprocessorport', 'requestreceiverport', 'sendsmsport', 'smppinterfaceport', 'smpploadbalancerport', 'smslogport')
    search_fields = ('containerport_id', 'portname')

@admin.register(ContainerRedisQueueDB)
class ContainerRedisQueueDBAdmin(admin.ModelAdmin):
    list_display = ('redisqueuedb_id', 'created_date', 'deploymentstatus', 'redisqueuedbname', 'runningstatus', 'update_date', 'gatewayip_id', 'gatewayport_id')
    search_fields = ('redisqueuedb_id', 'redisqueuedbname')

@admin.register(ContainerRequestProcessor)
class ContainerRequestProcessorAdmin(admin.ModelAdmin):
    list_display = ('requestprocessor_id', 'created_date', 'deploymentstatus', 'requestprocessorname', 'runningstatus', 'update_date', 'redisqueuedb_id', 'gatewayip_id', 'gatewayport_id')
    search_fields = ('requestprocessor_id', 'requestprocessorname')

@admin.register(ContainerSMPPInterface)
class ContainerSMPPInterfaceAdmin(admin.ModelAdmin):
    list_display = ('smppinterface_id', 'created_date', 'deploymentstatus', 'runningstatus', 'smppinterfacename', 'update_date', 'gatewayip_id', 'gatewayport_id')
    search_fields = ('smppinterface_id', 'smppinterfacename')

@admin.register(ContainerSMPPLoadBalancer)
class ContainerSMPPLoadBalancerAdmin(admin.ModelAdmin):
    list_display = ('smpploadbalancer_id', 'created_date', 'deploymentstatus', 'runningstatus', 'smpploadbalancername', 'update_date', 'gatewayip_id', 'gatewayport_id')
    search_fields = ('smpploadbalancer_id', 'smpploadbalancername')

@admin.register(ContainerTLVTag)
class ContainerTLVTagAdmin(admin.ModelAdmin):
    list_display = ('dlvtag_id', 'created_date', 'length', 'name', 'tag', 'type')
    search_fields = ('dlvtag_id', 'name', 'tag', 'type')
