from currency.views import (
    contactus_create, contactus_delete, contactus_details, contactus_list, contactus_update,
    rate_create, rate_delete, rate_details, rate_list, rate_update,
    source_create, source_delete, source_details, source_list, source_update,
)

from django.urls import path

app_name = 'currency'

urlpatterns = [
    path('rate/list/', rate_list, name='rate-list'),
    path('rate/details/<int:pk>/', rate_details, name='rate-details'),
    path('rate/create/', rate_create, name='rate-create'),
    path('rate/update/<int:pk>/', rate_update, name='rate-update'),
    path('rate/delete/<int:pk>/', rate_delete, name='rate-delete'),
    path('source/list/', source_list, name='source-list'),
    path('source/details/<int:pk>/', source_details, name='source-details'),
    path('source/create/', source_create, name='source-create'),
    path('source/update/<int:pk>/', source_update, name='source-update'),
    path('source/delete/<int:pk>/', source_delete, name='source-delete'),
    path('contactus/list/', contactus_list, name='contactus-list'),
    path('contactus/details/<int:pk>/', contactus_details, name='contactus-details'),
    path('contactus/create/', contactus_create, name='contactus-create'),
    path('contactus/update/<int:pk>/', contactus_update, name='contactus-update'),
    path('contactus/delete/<int:pk>/', contactus_delete, name='contactus-delete'),
]
