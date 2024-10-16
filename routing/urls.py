# urls.py
from django.urls import path
from .views import (
    RouteListView, RouteCreateView, RouteUpdateView,
    RouteAccountListView, RouteAccountCreateView, RouteAccountUpdateView,
    RouteAccountMncmccListView, RouteAccountMncmccCreateView, RouteAccountMncmccUpdateView,
    RouteCustomerListView, RouteCustomerCreateView, RouteCustomerUpdateView,
    RouteCustomerMncmccListView, RouteCustomerMncmccCreateView, RouteCustomerMncmccUpdateView,
    RouteSharedListView, RouteSharedCreateView, RouteSharedUpdateView,
    RouteSharedMncmccListView, RouteSharedMncmccCreateView, RouteSharedMncmccUpdateView
)

urlpatterns = [
    path('route/getall', RouteListView.as_view(), name='route-getall'),
    path('route/save', RouteCreateView.as_view(), name='route-create'),
    path('route/edit/', RouteUpdateView.as_view(), name='route-update'),

    path('routeaccount/getall', RouteAccountListView.as_view(), name='routeaccount-getall'),
    path('routeaccount/save', RouteAccountCreateView.as_view(), name='routeaccount-create'),
    path('routeaccount/edit', RouteAccountUpdateView.as_view(), name='routeaccount-update'),

    path('routeaccountmncmcc/getall', RouteAccountMncmccListView.as_view(), name='routeaccountmncmcc-getall'),
    path('routeaccountmncmcc/save', RouteAccountMncmccCreateView.as_view(), name='routeaccountmncmcc-create'),
    path('routeaccountmncmcc/edit', RouteAccountMncmccUpdateView.as_view(), name='routeaccountmncmcc-update'),

    path('routecustomer/getall', RouteCustomerListView.as_view(), name='routecustomer-getall'),
    path('routecustomer/save', RouteCustomerCreateView.as_view(), name='routecustomer-create'),
    path('routecustomer/edit', RouteCustomerUpdateView.as_view(), name='routecustomer-update'),

    path('routecustomermncmcc/getall', RouteCustomerMncmccListView.as_view(), name='routecustomermncmcc-getall'),
    path('routecustomermncmcc/save', RouteCustomerMncmccCreateView.as_view(), name='routecustomermncmcc-create'),
    path('routecustomermncmcc/edit', RouteCustomerMncmccUpdateView.as_view(), name='routecustomermncmcc-update'),



    path('routeshared/getall', RouteSharedListView.as_view(), name='routeshared-getall'),
    path('routeshared/save', RouteSharedCreateView.as_view(), name='routeshared-create'),
    path('routeshared/edit', RouteSharedUpdateView.as_view(), name='routeshared-update'),

    path('routesharedmncmcc/getall', RouteSharedMncmccListView.as_view(), name='routesharedmncmcc-getall'),
    path('routesharedmncmcc/save', RouteSharedMncmccCreateView.as_view(), name='routesharedmncmcc-create'),
    path('routesharedmncmcc/edit', RouteSharedMncmccUpdateView.as_view(), name='routesharedmncmcc-update'),
]
