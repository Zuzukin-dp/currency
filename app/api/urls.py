from django.urls import path

from api.views import RateViewSet, RateTypeChoiceView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'rates', RateViewSet, basename='rate')
urlpatterns = [
    path('choices/currency/types/', RateTypeChoiceView.as_view(), name='choices-currency-types')
]
urlpatterns += router.urls
