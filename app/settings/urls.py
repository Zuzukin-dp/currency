from currency.views import generate_pass, requirements

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),

    path('gen_pass/', generate_pass),
    path('requirements/', requirements),

]
