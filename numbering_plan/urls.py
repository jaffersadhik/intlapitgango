from django.urls import path
from .views import (
    CountryListView, CountryCreateView, CountryUpdateView,
    MncMccListView, MncMccCreateView, MncMccUpdateView,
    MncMccPrefixListView, MncMccPrefixCreateView, MncMccPrefixUpdateView,
    WorldTimezoneListView, WorldTimezoneCreateView, WorldTimezoneUpdateView
)

urlpatterns = [
    # Country URLs
    path('country/getall', CountryListView.as_view(), name='country-getall'),
    path('country/save', CountryCreateView.as_view(), name='country-create'),
    path('country/edit', CountryUpdateView.as_view(), name='country-update'),

    # MncMcc URLs
    path('mncmcc/getall', MncMccListView.as_view(), name='mncmcc-getall'),
    path('mncmcc/save', MncMccCreateView.as_view(), name='mncmcc-create'),
    path('mncmcc/edit', MncMccUpdateView.as_view(), name='mncmcc-update'),

    # MncMccPrefix URLs
    path('mncmccprefix/getall', MncMccPrefixListView.as_view(), name='mncmccprefix-getall'),
    path('mncmccprefix/save', MncMccPrefixCreateView.as_view(), name='mncmccprefix-create'),
    path('mncmccprefix/edit', MncMccPrefixUpdateView.as_view(), name='mncmccprefix-update'),

    # WorldTimezone URLs
    path('worldtimezone/getall', WorldTimezoneListView.as_view(), name='worldtimezone-getall'),
    path('worldtimezone/save', WorldTimezoneCreateView.as_view(), name='worldtimezone-create'),
    path('worldtimezone/edit', WorldTimezoneUpdateView.as_view(), name='worldtimezone-update'),
]
