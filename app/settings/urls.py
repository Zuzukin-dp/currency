from currency.views import index

import debug_toolbar

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', index, name='index'),
    path('currency/', include('currency.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]
