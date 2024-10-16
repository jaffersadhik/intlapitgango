from django.urls import path
from .views import (
    CostCarrierListView,
    CostCarrierCreateView,
    CostCarrierUpdateView,
    CostCarrierInvoiceDateListView,
    CostCarrierInvoiceDateCreateView,
    CostCarrierInvoiceDateUpdateView,
    CostCarrierMncmccListView,
    CostCarrierMncmccCreateView,
    CostCarrierMncmccUpdateView,
    CostCarrierMncmccInvoiceDateListView,
    CostCarrierMncmccInvoiceDateCreateView,
    CostCarrierMncmccInvoiceDateUpdateView,
    CostSMSCListView,
    CostSMSCCreateView,
    CostSMSCUpdateView,
    CostSMSCInvoiceDateListView,
    CostSMSCInvoiceDateCreateView,
    CostSMSCInvoiceDateUpdateView,
    CostSMSCmncmccListView,
    CostSMSCmncmccCreateView,
    CostSMSCmncmccUpdateView,
    CostSMSCmncmccInvoiceDateListView,
    CostSMSCmncmccInvoiceDateCreateView,
    CostSMSCmncmccInvoiceDateUpdateView,
)

urlpatterns = [
    # CostCarrier URLs
    path('cost-carrier', CostCarrierListView.as_view(), name='cost-carrier-list'),
    path('cost-carrier/create', CostCarrierCreateView.as_view(), name='cost-carrier-create'),
    path('cost-carrier/update', CostCarrierUpdateView.as_view(), name='cost-carrier-update'),

    # CostCarrierInvoiceDate URLs
    path('cost-carrier-invoice-date', CostCarrierInvoiceDateListView.as_view(), name='cost-carrier-invoice-date-list'),
    path('cost-carrier-invoice-date/create', CostCarrierInvoiceDateCreateView.as_view(), name='cost-carrier-invoice-date-create'),
    path('cost-carrier-invoice-date/update', CostCarrierInvoiceDateUpdateView.as_view(), name='cost-carrier-invoice-date-update'),

    # CostCarrierMncmcc URLs
    path('cost-carrier-mncmcc', CostCarrierMncmccListView.as_view(), name='cost-carrier-mncmcc-list'),
    path('cost-carrier-mncmcc/create', CostCarrierMncmccCreateView.as_view(), name='cost-carrier-mncmcc-create'),
    path('cost-carrier-mncmcc/update', CostCarrierMncmccUpdateView.as_view(), name='cost-carrier-mncmcc-update'),

    # CostCarrierMncmccInvoiceDate URLs
    path('cost-carrier-mncmcc-invoice-date', CostCarrierMncmccInvoiceDateListView.as_view(), name='cost-carrier-mncmcc-invoice-date-list'),
    path('cost-carrier-mncmcc-invoice-date/create', CostCarrierMncmccInvoiceDateCreateView.as_view(), name='cost-carrier-mncmcc-invoice-date-create'),
    path('cost-carrier-mncmcc-invoice-date/update', CostCarrierMncmccInvoiceDateUpdateView.as_view(), name='cost-carrier-mncmcc-invoice-date-update'),

    # CostSMSC URLs
    path('cost-smsc', CostSMSCListView.as_view(), name='cost-smsc-list'),
    path('cost-smsc/create', CostSMSCCreateView.as_view(), name='cost-smsc-create'),
    path('cost-smsc/update', CostSMSCUpdateView.as_view(), name='cost-smsc-update'),

    # CostSMSCInvoiceDate URLs
    path('cost-smsc-invoice-date', CostSMSCInvoiceDateListView.as_view(), name='cost-smsc-invoice-date-list'),
    path('cost-smsc-invoice-date/create', CostSMSCInvoiceDateCreateView.as_view(), name='cost-smsc-invoice-date-create'),
    path('cost-smsc-invoice-date/update', CostSMSCInvoiceDateUpdateView.as_view(), name='cost-smsc-invoice-date-update'),

    # CostSMSCmncmcc URLs
    path('cost-smsc-mncmcc', CostSMSCmncmccListView.as_view(), name='cost-smsc-mncmcc-list'),
    path('cost-smsc-mncmcc/create', CostSMSCmncmccCreateView.as_view(), name='cost-smsc-mncmcc-create'),
    path('cost-smsc-mncmcc/update', CostSMSCmncmccUpdateView.as_view(), name='cost-smsc-mncmcc-update'),

    # CostSMSCmncmccInvoiceDate URLs
    path('cost-smsc-mncmcc-invoice-date', CostSMSCmncmccInvoiceDateListView.as_view(), name='cost-smsc-mncmcc-invoice-date-list'),
    path('cost-smsc-mncmcc-invoice-date/create', CostSMSCmncmccInvoiceDateCreateView.as_view(), name='cost-smsc-mncmcc-invoice-date-create'),
    path('cost-smsc-mncmcc-invoice-date/update', CostSMSCmncmccInvoiceDateUpdateView.as_view(), name='cost-smsc-mncmcc-invoice-date-update'),
]
