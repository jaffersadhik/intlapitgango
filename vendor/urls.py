from django.urls import path
from .views import (
    CarrierListView, CarrierCreateView, CarrierUpdateView,
    SMSCListView, SMSCCreateView, SMSCUpdateView,
    DataCenterListView, DataCenterCreateView, DataCenterUpdateView,
    KannelHostListView, KannelHostCreateView, KannelHostUpdateView,
    DCSmscidListView, DCSmscidCreateView, DCSmscidUpdateView
)

urlpatterns = [
    # Carrier URLs
    path('carrier/getall/', CarrierListView.as_view(), name='carrier-getall'),
    path('carrier/save/', CarrierCreateView.as_view(), name='carrier-create'),
    path('carrier/edit/', CarrierUpdateView.as_view(), name='carrier-update'),

    # SMSC URLs
    path('smsc/getall/', SMSCListView.as_view(), name='smsc-getall'),
    path('smsc/save/', SMSCCreateView.as_view(), name='smsc-create'),
    path('smsc/edit/', SMSCUpdateView.as_view(), name='smsc-update'),


    path('datacenter/getall/', DataCenterListView.as_view(), name='datacenter-getall'),
    path('datacenter/save/', DataCenterCreateView.as_view(), name='datacenter-create'),
    path('datacenter/edit/', DataCenterUpdateView.as_view(), name='datacenter-update'),

    path('kannelhost/getall/', KannelHostListView.as_view(), name='kannelhost-getall'),
    path('kannelhost/save/', KannelHostCreateView.as_view(), name='kannelhost-create'),
    path('kannelhost/edit/', KannelHostUpdateView.as_view(), name='kannelhost-update'),

    path('dc_smscid/getall/', DCSmscidListView.as_view(), name='dcsmscid-getall'),
    path('dc_smscid/save/', DCSmscidCreateView.as_view(), name='dcsmscid-create'),
    path('dc_smscid/edit/', DCSmscidUpdateView.as_view(), name='dcsmscid-update'),
]
