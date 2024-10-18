from django.urls import path
from .views import WebhookAccountListView, WebhookAccountCreateView, WebhookAccountUpdateView
from .views import WebhookCustomerListView, WebhookCustomerCreateView, WebhookCustomerUpdateView
from .views import WebhookParameterIndexListView, WebhookParameterIndexCreateView, WebhookParameterIndexUpdateView

urlpatterns = [
    path('webhookaccount/getall', WebhookAccountListView.as_view(), name='webhookaccount-getall'),
    path('webhookaccount/save', WebhookAccountCreateView.as_view(), name='webhookaccount-create'),
    path('webhookaccount/edit', WebhookAccountUpdateView.as_view(), name='webhookaccount-update'),
    
    path('webhookcustomer/getall', WebhookCustomerListView.as_view(), name='webhookcustomer-getall'),
    path('webhookcustomer/save', WebhookCustomerCreateView.as_view(), name='webhookcustomer-create'),
    path('webhookcustomer/edit', WebhookCustomerUpdateView.as_view(), name='webhookcustomer-update'),

    path('webhookparameter/getall', WebhookParameterIndexListView.as_view(), name='webhookparameter-getall'),
    path('webhookparameter/save', WebhookParameterIndexCreateView.as_view(), name='webhookparameter-create'),
    path('webhookparameter/edit', WebhookParameterIndexUpdateView.as_view(), name='webhookparameter-update'),
]
