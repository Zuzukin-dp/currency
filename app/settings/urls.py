from currency.views import (
    contactus_create, contactus_delete, contactus_details, contactus_list, contactus_update,
    generate_pass,
    index,
    rate_create, rate_delete, rate_details, rate_list, rate_update,
    requirements,
    source_create, source_delete, source_details, source_list, source_update,
)

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),

    path('gen_pass/', generate_pass),
    path('requirements/', requirements),
    path('currency/rate/list/', rate_list, name='rate-list'),
    path('currency/rate/details/<int:pk>/', rate_details, name='rate-details'),
    path('currency/rate/create/', rate_create, name='rate-create'),
    path('currency/rate/update/<int:pk>/', rate_update, name='rate-update'),
    path('currency/rate/delete/<int:pk>/', rate_delete, name='rate-delete'),
    path('currency/source/list/', source_list, name='source-list'),
    path('currency/source/details/<int:pk>/', source_details, name='source-details'),
    path('currency/source/create/', source_create, name='source-create'),
    path('currency/source/update/<int:pk>/', source_update, name='source-update'),
    path('currency/source/delete/<int:pk>/', source_delete, name='source-delete'),
    path('currency/contactus/list/', contactus_list, name='contactus-list'),
    path('currency/contactus/details/<int:pk>/', contactus_details, name='contactus-details'),
    path('currency/contactus/create/', contactus_create, name='contactus-create'),
    path('currency/contactus/update/<int:pk>/', contactus_update, name='contactus-update'),
    path('currency/contactus/delete/<int:pk>/', contactus_delete, name='contactus-delete'),

]
