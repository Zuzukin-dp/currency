from currency.views import (
    AnalyticsView,
    ContactUsDeleteView, ContactUsDetailView, ContactUsListView, ContactUsUpdateView,
    CreateContactUs, CreateRate, CreateSource, RateDeleteView, RateDetailView,
    RateListView, RateUpdateView, SourceDeleteView, SourceDetailView, SourceListView,
    SourceUpdateView, LatestRates
)

from django.urls import path

app_name = 'currency'

urlpatterns = [
    path('rate/latest/', LatestRates.as_view(), name='rate-latest'),
    path('rate/list/', RateListView.as_view(), name='rate-list'),
    path('rate/details/<int:pk>/', RateDetailView.as_view(), name='rate-details'),
    path('rate/create/', CreateRate.as_view(), name='rate-create'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),

    path('source/list/', SourceListView.as_view(), name='source-list'),
    path('source/details/<int:pk>/', SourceDetailView.as_view(), name='source-details'),
    path('source/create/', CreateSource.as_view(), name='source-create'),
    path('source/update/<int:pk>/', SourceUpdateView.as_view(), name='source-update'),
    path('source/delete/<int:pk>/', SourceDeleteView.as_view(), name='source-delete'),

    path('contactus/list/', ContactUsListView.as_view(), name='contactus-list'),
    path('contactus/details/<int:pk>/', ContactUsDetailView.as_view(), name='contactus-details'),
    path('contactus/create/', CreateContactUs.as_view(), name='contactus-create'),
    path('contactus/update/<int:pk>/', ContactUsUpdateView.as_view(), name='contactus-update'),
    path('contactus/delete/<int:pk>/', ContactUsDeleteView.as_view(), name='contactus-delete'),

    path('analytics/list/', AnalyticsView.as_view(), name='analytics-list'),

]
