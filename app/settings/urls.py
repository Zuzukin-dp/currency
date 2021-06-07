from currency.views import (generate_pass,
                            rate_list,
                            requirements,
                            rate_details,
                            source_list,
                            source_details
                            )

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),

    # path('gen_pass/', generate_pass),
    # path('requirements/', requirements),
    path('rate/list/', rate_list),
    path('rate/details/<int:pk>/', rate_details),
    path('source/list/', source_list),
    path('source/details/<int:pk>/', source_details),

]
