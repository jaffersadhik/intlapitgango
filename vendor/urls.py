from django.urls import path
from .views import (
    CarrierListView, CarrierCreateView, CarrierUpdateView,
    SMSCListView, SMSCCreateView, SMSCUpdateView
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
]
