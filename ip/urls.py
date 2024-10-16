from django.urls import path
from .views import (
    IpAccountListView, IpAccountCreateView, IpAccountUpdateView,
    IpCustomerListView, IpCustomerCreateView, IpCustomerUpdateView,
    IpSharedListView, IpSharedCreateView, IpSharedUpdateView
)

urlpatterns = [
    # IP Account URLs
    path('ipaccount/getall/', IpAccountListView.as_view(), name='ipaccount-getall'),
    path('ipaccount/save/', IpAccountCreateView.as_view(), name='ipaccount-create'),
    path('ipaccount/edit/', IpAccountUpdateView.as_view(), name='ipaccount-update'),

    # IP Customer URLs
    path('ipcustomer/getall/', IpCustomerListView.as_view(), name='ipcustomer-getall'),
    path('ipcustomer/save/', IpCustomerCreateView.as_view(), name='ipcustomer-create'),
    path('ipcustomer/edit/', IpCustomerUpdateView.as_view(), name='ipcustomer-update'),

    # IP Shared URLs
    path('ipshared/getall/', IpSharedListView.as_view(), name='ipshared-getall'),
    path('ipshared/save/', IpSharedCreateView.as_view(), name='ipshared-create'),
    path('ipshared/edit/', IpSharedUpdateView.as_view(), name='ipshared-update'),
]
