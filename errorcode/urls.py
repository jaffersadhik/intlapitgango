from django.urls import path
from .views import (
    ErrorcodeAccountListView,
    ErrorcodeAccountCreateView,
    ErrorcodeAccountUpdateView,
    ErrorcodeCarrierListView,
    ErrorcodeCarrierCreateView,
    ErrorcodeCarrierUpdateView,
    ErrorcodePlatformListView,
    ErrorcodePlatformCreateView,
    ErrorcodePlatformUpdateView,
    ErrorcodeCustomerListView,
    ErrorcodeCustomerCreateView,
    ErrorcodeCustomerUpdateView,
    ErrorcodeSmsServiceProviderListView,
    ErrorcodeSmsServiceProviderCreateView,
    ErrorcodeSmsServiceProviderUpdateView
)

urlpatterns = [
    # URLs for ErrorcodeAccount
    path('errorcodeaccount/getall', ErrorcodeAccountListView.as_view(), name='errorcodeaccount-getall'),
    path('errorcodeaccount/save', ErrorcodeAccountCreateView.as_view(), name='errorcodeaccount-create'),
    path('errorcodeaccount/edit', ErrorcodeAccountUpdateView.as_view(), name='errorcodeaccount-update'),

    # URLs for ErrorcodeCarrier
    path('errorcodecarrier/getall', ErrorcodeCarrierListView.as_view(), name='errorcodecarrier-getall'),
    path('errorcodecarrier/save', ErrorcodeCarrierCreateView.as_view(), name='errorcodecarrier-create'),
    path('errorcodecarrier/edit', ErrorcodeCarrierUpdateView.as_view(), name='errorcodecarrier-update'),

    # URLs for ErrorcodePlatform
    path('errorcodeplatform/getall', ErrorcodePlatformListView.as_view(), name='errorcodeplatform-getall'),
    path('errorcodeplatform/save', ErrorcodePlatformCreateView.as_view(), name='errorcodeplatform-create'),
    path('errorcodeplatform/edit', ErrorcodePlatformUpdateView.as_view(), name='errorcodeplatform-update'),




    path('errorcodecustomer/getall', ErrorcodeCustomerListView.as_view(), name='errorcodecustomer-getall'),
    path('errorcodecustomer/save', ErrorcodeCustomerCreateView.as_view(), name='errorcodecustomer-create'),
    path('errorcodecustomer/edit', ErrorcodeCustomerUpdateView.as_view(), name='errorcodecustomer-update'),


    path('smsserviceprovider/getall', ErrorcodeSmsServiceProviderListView.as_view(), name='smsserviceprovider-getall'),
    path('smsserviceprovider/save', ErrorcodeSmsServiceProviderCreateView.as_view(), name='smsserviceprovider-create'),
    path('smsserviceprovider/edit', ErrorcodeSmsServiceProviderUpdateView.as_view(), name='smsserviceprovider-update'),



]
