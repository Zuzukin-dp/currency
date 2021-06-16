from currency.views import (
    ContactUsLitView, ContactUsDeleteView, ContactUsDetailView, ContactUsUpdateView, CreateContactUs,
    CreateRate, RateDeleteView, RateDetailView, RateLitView, RateUpdateView,
    CreateSource, SourceDeleteView, SourceDetailView, SourceLitView, SourceUpdateView,
)

from django.urls import path

app_name = 'currency'

urlpatterns = [
    path('rate/list/', RateLitView.as_view(), name='rate-list'),
    path('rate/details/<int:pk>/', RateDetailView.as_view(), name='rate-details'),
    path('rate/create/', CreateRate.as_view(), name='rate-create'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),

    path('source/list/', SourceLitView.as_view(), name='source-list'),
    path('source/details/<int:pk>/', SourceDetailView.as_view(), name='source-details'),
    path('source/create/', CreateSource.as_view(), name='source-create'),
    path('source/update/<int:pk>/', SourceUpdateView.as_view(), name='source-update'),
    path('source/delete/<int:pk>/', SourceDeleteView.as_view(), name='source-delete'),

    path('contactus/list/', ContactUsLitView.as_view(), name='contactus-list'),
    path('contactus/details/<int:pk>/', ContactUsDetailView.as_view(), name='contactus-details'),
    path('contactus/create/', CreateContactUs.as_view(), name='contactus-create'),
    path('contactus/update/<int:pk>/', ContactUsUpdateView.as_view(), name='contactus-update'),
    path('contactus/delete/<int:pk>/', ContactUsDeleteView.as_view(), name='contactus-delete'),
]
