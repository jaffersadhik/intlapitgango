from django.urls import path
from .views import (
    PaymentListView,
    PaymentCreateView,
    PaymentUpdateView,
    InvoiceListView,
    InvoiceCreateView,
    InvoiceUpdateView,
    OutstandingListView,
    OutstandingCreateView,
    OutstandingUpdateView,
)

urlpatterns = [
    # Payment URLs
    path('payment/getall', PaymentListView.as_view(), name='payment-getall'),
    path('payment/save', PaymentCreateView.as_view(), name='payment-create'),
    path('payment/edit', PaymentUpdateView.as_view(), name='payment-update'),

    # Invoice URLs
    path('invoice/getall', InvoiceListView.as_view(), name='invoice-getall'),
    path('invoice/save', InvoiceCreateView.as_view(), name='invoice-create'),
    path('invoice/edit', InvoiceUpdateView.as_view(), name='invoice-update'),

    # Outstanding URLs
    path('outstanding/getall', OutstandingListView.as_view(), name='outstanding-getall'),
    path('outstanding/save', OutstandingCreateView.as_view(), name='outstanding-create'),
    path('outstanding/edit', OutstandingUpdateView.as_view(), name='outstanding-update'),
]
