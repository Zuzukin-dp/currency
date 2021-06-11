from currency.views import (
    contactus_create, contactus_details, contactus_delete, contactus_list, contactus_update,
    generate_pass,
    rate_create, rate_details, rate_delete, rate_update, rate_list,
    requirements,
    source_create, source_details, source_delete, source_list, source_update,
)

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),

    path('gen_pass/', generate_pass),
    path('requirements/', requirements),
    path('currency/rate/list/', rate_list),
    path('currency/rate/details/<int:pk>/', rate_details),
    path('currency/rate/create/', rate_create),
    path('currency/rate/update/<int:pk>/', rate_update),
    path('currency/rate/delete/<int:pk>/', rate_delete),
    path('currency/source/list/', source_list),
    path('currency/source/details/<int:pk>/', source_details),
    path('currency/source/create/', source_create),
    path('currency/source/update/<int:pk>/', source_update),
    path('currency/source/delete/<int:pk>/', source_delete),
    path('currency/contactus/list/', contactus_list),
    path('currency/contactus/details/<int:pk>/', contactus_details),
    path('currency/contactus/create/', contactus_create),
    path('currency/contactus/update/<int:pk>/', contactus_update),
    path('currency/contactus/delete/<int:pk>/', contactus_delete),

]
