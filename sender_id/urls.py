from django.urls import path
from .views import (
    SenderIdAccountListView, SenderIdAccountCreateView, SenderIdAccountUpdateView,
    SenderIdCustomerListView, SenderIdCustomerCreateView, SenderIdCustomerUpdateView,
    SenderIdSharedListView, SenderIdSharedCreateView, SenderIdSharedUpdateView
)

urlpatterns = [
    # SenderIdAccount URLs
    path('senderidaccount/getall/', SenderIdAccountListView.as_view(), name='senderidaccount-getall'),
    path('senderidaccount/save/', SenderIdAccountCreateView.as_view(), name='senderidaccount-create'),
    path('senderidaccount/edit/', SenderIdAccountUpdateView.as_view(), name='senderidaccount-update'),

    # SenderIdCustomer URLs
    path('senderidcustomer/getall/', SenderIdCustomerListView.as_view(), name='senderidcustomer-getall'),
    path('senderidcustomer/save/', SenderIdCustomerCreateView.as_view(), name='senderidcustomer-create'),
    path('senderidcustomer/edit/', SenderIdCustomerUpdateView.as_view(), name='senderidcustomer-update'),

    # SenderIdShared URLs
    path('senderidshared/getall/', SenderIdSharedListView.as_view(), name='senderidshared-getall'),
    path('senderidshared/save/', SenderIdSharedCreateView.as_view(), name='senderidshared-create'),
    path('senderidshared/edit/', SenderIdSharedUpdateView.as_view(), name='senderidshared-update'),
]
