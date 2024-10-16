from django.urls import path
from .views import (
    AccountListView, AccountCreateView, AccountUpdateView,
    CompanyListView, CompanyCreateView, CompanyUpdateView,
    CustomerListView, CustomerCreateView, CustomerUpdateView
)

urlpatterns = [
    # Account URLs
    path('account/getall', AccountListView.as_view(), name='account-getall'),
    path('account/save', AccountCreateView.as_view(), name='account-create'),
    path('account/edit', AccountUpdateView.as_view(), name='account-update'),

    # Company URLs
    path('company/getall', CompanyListView.as_view(), name='company-getall'),
    path('company/save', CompanyCreateView.as_view(), name='company-create'),
    path('company/edit', CompanyUpdateView.as_view(), name='company-update'),

    # Customer URLs
    path('customer/getall', CustomerListView.as_view(), name='customer-getall'),
    path('customer/save', CustomerCreateView.as_view(), name='customer-create'),
    path('customer/edit', CustomerUpdateView.as_view(), name='customer-update'),
]
