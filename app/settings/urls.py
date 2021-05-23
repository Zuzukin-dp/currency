from django.contrib import admin
from django.urls import path

from currency.views import generate_pass, requirements


urlpatterns = [
    path('admin/', admin.site.urls),

    path('gen_pass/', generate_pass),
    path('requirements/', requirements),

]
