from django.urls import path
from .views import (
    PriceAccountListView,
    PriceAccountCreateView,
    PriceAccountUpdateView,
    PriceAccountInvoiceDateListView,
    PriceAccountInvoiceDateCreateView,
    PriceAccountInvoiceDateUpdateView,
    PriceAccountMncmccListView,
    PriceAccountMncmccCreateView,
    PriceAccountMncmccUpdateView,
    PriceAccountMncmccInvoiceDateListView,
    PriceAccountMncmccInvoiceDateCreateView,
    PriceAccountMncmccInvoiceDateUpdateView,
    PriceCustomerListView,
    PriceCustomerCreateView,
    PriceCustomerUpdateView,
    PriceCustomerInvoiceDateListView,
    PriceCustomerInvoiceDateCreateView,
    PriceCustomerInvoiceDateUpdateView,
    PriceCustomerMncmccListView,
    PriceCustomerMncmccCreateView,
    PriceCustomerMncmccUpdateView,
    PriceCustomerMncmccInvoiceDateListView,
    PriceCustomerMncmccInvoiceDateCreateView,
    PriceCustomerMncmccInvoiceDateUpdateView,
    PriceSharedListView,
    PriceSharedCreateView,
    PriceSharedUpdateView,
    PriceSharedInvoiceDateListView,
    PriceSharedInvoiceDateCreateView,
    PriceSharedInvoiceDateUpdateView,
    PriceSharedMncmccListView,
    PriceSharedMncmccCreateView,
    PriceSharedMncmccUpdateView,
    PriceSharedMncmccInvoiceDateListView,
    PriceSharedMncmccInvoiceDateCreateView,
    PriceSharedMncmccInvoiceDateUpdateView
)

urlpatterns = [
    # PriceAccount URLs
    path('price-accounts', PriceAccountListView.as_view(), name='price_account_list'),
    path('price-accounts/create', PriceAccountCreateView.as_view(), name='price_account_create'),
    path('price-account/update', PriceAccountUpdateView.as_view(), name='price_account_update'),

    # PriceAccountInvoiceDate URLs
    path('price-account-invoice-dates', PriceAccountInvoiceDateListView.as_view(), name='price_account_invoice_date_list'),
    path('price-account-invoice-dates/create', PriceAccountInvoiceDateCreateView.as_view(), name='price_account_invoice_date_create'),
    path('price-account-invoice-dates/update', PriceAccountInvoiceDateUpdateView.as_view(), name='price_account_invoice_date_update'),

    # PriceAccountMncmcc URLs
    path('price-account-mncmccs', PriceAccountMncmccListView.as_view(), name='price_account_mncmcc_list'),
    path('price-account-mncmccs/create', PriceAccountMncmccCreateView.as_view(), name='price_account_mncmcc_create'),
    path('price-account-mncmcc/update', PriceAccountMncmccUpdateView.as_view(), name='price_account_mncmcc_update'),

    # PriceAccountMncmccInvoiceDate URLs
    path('price-account-mncmcc-invoice-dates', PriceAccountMncmccInvoiceDateListView.as_view(), name='price_account_mncmcc_invoice_date_list'),
    path('price-account-mncmcc-invoice-dates/create', PriceAccountMncmccInvoiceDateCreateView.as_view(), name='price_account_mncmcc_invoice_date_create'),
    path('price-account-mncmcc-invoice-date/update', PriceAccountMncmccInvoiceDateUpdateView.as_view(), name='price_account_mncmcc_invoice_date_update'),

    # PriceCustomer URLs
    path('price-customers', PriceCustomerListView.as_view(), name='price_customer_list'),
    path('price-customers/create', PriceCustomerCreateView.as_view(), name='price_customer_create'),
    path('price-customer/update', PriceCustomerUpdateView.as_view(), name='price_customer_update'),

    # PriceCustomerInvoiceDate URLs
    path('price-customer-invoice-dates', PriceCustomerInvoiceDateListView.as_view(), name='price_customer_invoice_date_list'),
    path('price-customer-invoice-dates/create', PriceCustomerInvoiceDateCreateView.as_view(), name='price_customer_invoice_date_create'),
    path('price-customer-invoice-date/update', PriceCustomerInvoiceDateUpdateView.as_view(), name='price_customer_invoice_date_update'),

    # PriceCustomerMncmcc URLs
    path('price/customer/mncmcc', PriceCustomerMncmccListView.as_view(), name='price_customer_mncmcc_list'),
    path('price/customer/mncmcc/create', PriceCustomerMncmccCreateView.as_view(), name='price_customer_mncmcc_create'),
    path('price/customer/mncmcc/update', PriceCustomerMncmccUpdateView.as_view(), name='price_customer_mncmcc_update'),
    
    # PriceCustomerMncmccInvoiceDate URLs
    path('price/customer/mncmcc/invoice_date', PriceCustomerMncmccInvoiceDateListView.as_view(), name='price_customer_mncmcc_invoice_date_list'),
    path('price/customer/mncmcc/invoice_date/create', PriceCustomerMncmccInvoiceDateCreateView.as_view(), name='price_customer_mncmcc_invoice_date_create'),
    path('price/customer/mncmcc/invoice_date/update', PriceCustomerMncmccInvoiceDateUpdateView.as_view(), name='price_customer_mncmcc_invoice_date_update'),

    # PriceShared URLs
    path('price/shared', PriceSharedListView.as_view(), name='price_shared_list'),
    path('price/shared/create', PriceSharedCreateView.as_view(), name='price_shared_create'),
    path('price/shared/update', PriceSharedUpdateView.as_view(), name='price_shared_update'),

    # PriceSharedInvoiceDate URLs
    path('price/shared/invoice_date', PriceSharedInvoiceDateListView.as_view(), name='price_shared_invoice_date_list'),
    path('price/shared/invoice_date/create', PriceSharedInvoiceDateCreateView.as_view(), name='price_shared_invoice_date_create'),
    path('price/shared/invoice_date/update', PriceSharedInvoiceDateUpdateView.as_view(), name='price_shared_invoice_date_update'),

    # PriceSharedMncmcc URLs
    path('price/shared/mncmcc', PriceSharedMncmccListView.as_view(), name='price_shared_mncmcc_list'),
    path('price/shared/mncmcc/create', PriceSharedMncmccCreateView.as_view(), name='price_shared_mncmcc_create'),
    path('price/shared/mncmcc/update', PriceSharedMncmccUpdateView.as_view(), name='price_shared_mncmcc_update'),

    # PriceSharedMncmccInvoiceDate URLs
    path('price/shared/mncmcc/invoice_date', PriceSharedMncmccInvoiceDateListView.as_view(), name='price_shared_mncmcc_invoice_date_list'),
    path('price/shared/mncmcc/invoice_date/create', PriceSharedMncmccInvoiceDateCreateView.as_view(), name='price_shared_mncmcc_invoice_date_create'),
    path('price/shared/mncmcc/invoice_date/update', PriceSharedMncmccInvoiceDateUpdateView.as_view(), name='price_shared_mncmcc_invoice_date_update'),
]
