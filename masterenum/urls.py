from django.urls import path
from .views import (
    IPCheckListView, IPCheckCreateView, IPCheckUpdateView,
    MNCMCCCheckListView, MNCMCCCheckCreateView, MNCMCCCheckUpdateView,
    InvoiceTypeListView, InvoiceTypeCreateView, InvoiceTypeUpdateView,
    ProtocolListView, ProtocolCreateView, ProtocolUpdateView,
    RouteCheckListView, RouteCheckCreateView, RouteCheckUpdateView,
    RouteTypeListView, RouteTypeCreateView, RouteTypeUpdateView,
    SenderIdCheckListView, SenderIdCheckCreateView, SenderIdCheckUpdateView,
    SmsTypeListView, SmsTypeCreateView, SmsTypeUpdateView,
    StatusListView, StatusCreateView, StatusUpdateView,
    PriceCheckListView, PriceCheckCreateView, PriceCheckUpdateView,
    SmsServiceProviderListView, SmsServiceProviderCreateView, SmsServiceProviderUpdateView
)

urlpatterns = [
    # IPCheck URLs
    path('ipcheck/getall', IPCheckListView.as_view(), name='ipcheck-getall'),
    path('ipcheck/save', IPCheckCreateView.as_view(), name='ipcheck-create'),
    path('ipcheck/edit', IPCheckUpdateView.as_view(), name='ipcheck-update'),

    # MNCMCCCheck URLs
    path('mncmcccheck/getall', MNCMCCCheckListView.as_view(), name='mncmcccheck-getall'),
    path('mncmcccheck/save', MNCMCCCheckCreateView.as_view(), name='mncmcccheck-create'),
    path('mncmcccheck/edit', MNCMCCCheckUpdateView.as_view(), name='mncmcccheck-update'),

    # InvoiceType URLs
    path('invoicetype/getall', InvoiceTypeListView.as_view(), name='invoicetype-getall'),
    path('invoicetype/save', InvoiceTypeCreateView.as_view(), name='invoicetype-create'),
    path('invoicetype/edit', InvoiceTypeUpdateView.as_view(), name='invoicetype-update'),

    # Protocol URLs
    path('protocol/getall', ProtocolListView.as_view(), name='protocol-getall'),
    path('protocol/save', ProtocolCreateView.as_view(), name='protocol-create'),
    path('protocol/edit', ProtocolUpdateView.as_view(), name='protocol-update'),

    # RouteCheck URLs
    path('routecheck/getall', RouteCheckListView.as_view(), name='routecheck-getall'),
    path('routecheck/save', RouteCheckCreateView.as_view(), name='routecheck-create'),
    path('routecheck/edit', RouteCheckUpdateView.as_view(), name='routecheck-update'),

    # RouteType URLs
    path('routetype/getall', RouteTypeListView.as_view(), name='routetype-getall'),
    path('routetype/save', RouteTypeCreateView.as_view(), name='routetype-create'),
    path('routetype/edit', RouteTypeUpdateView.as_view(), name='routetype-update'),

    # SenderIdCheck URLs
    path('senderidcheck/getall', SenderIdCheckListView.as_view(), name='senderidcheck-getall'),
    path('senderidcheck/save', SenderIdCheckCreateView.as_view(), name='senderidcheck-create'),
    path('senderidcheck/edit', SenderIdCheckUpdateView.as_view(), name='senderidcheck-update'),

    # SmsType URLs
    path('smstype/getall', SmsTypeListView.as_view(), name='smstype-getall'),
    path('smstype/save', SmsTypeCreateView.as_view(), name='smstype-create'),
    path('smstype/edit', SmsTypeUpdateView.as_view(), name='smstype-update'),

    # Status URLs
    path('status/getall', StatusListView.as_view(), name='status-getall'),
    path('status/save', StatusCreateView.as_view(), name='status-create'),
    path('status/edit', StatusUpdateView.as_view(), name='status-update'),

    # PriceCheck URLs
    path('pricecheck/getall', PriceCheckListView.as_view(), name='pricecheck-getall'),
    path('pricecheck/save', PriceCheckCreateView.as_view(), name='pricecheck-create'),
    path('pricecheck/edit', PriceCheckUpdateView.as_view(), name='pricecheck-update'),


    path('smsserviceprovidermain/getall', SmsServiceProviderListView.as_view(), name='smsserviceprovider-getall'),
    path('smsserviceprovidermain/save', SmsServiceProviderCreateView.as_view(), name='smsserviceprovider-create'),
    path('smsserviceprovidermai/edit', SmsServiceProviderUpdateView.as_view(), name='smsserviceprovider-update'),
]
