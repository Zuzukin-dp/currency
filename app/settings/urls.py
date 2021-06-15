from currency.views import index

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('currency/', include('currency.urls')),
]
