from currency.views import index
from django.conf.urls.static import static

import debug_toolbar

from django.contrib import admin
from django.urls import include, path
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', index, name='index'),
    path('auth/', include('django.contrib.auth.urls')),
    path('currency/', include('currency.urls')),
    path('accounts/', include('accounts.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
