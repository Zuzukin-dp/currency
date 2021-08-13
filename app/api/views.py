# from rest_framework import generics
from api.throttles import AnonUserRateThrottle
from currency.models import Rate
from currency import choices
from api.serializers import RateSerializer, RateDetailsSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from api.pagination import RatePagination
from api.filters import RateFilter
from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters
from django.shortcuts import render


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all().select_related('bank').order_by('-created')
    # serializer_class = RateSerializer
    pagination_class = RatePagination
    filterset_class = RateFilter
    throttle_classes = [AnonUserRateThrottle]
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    ordering_fields = ['id', 'created', 'cur_type', 'sale', 'buy']

    def get_serializer_class(self):
        if 'pk' in self.kwargs:
            return RateDetailsSerializer
        return RateSerializer


class RateTypeChoiceView(APIView):
    def get(self, request, format=None):
        return Response(choices.RATE_TYPE_CHOICES)


def api_list_page(request):
    return render(request, 'api_list.html')


# class RateList(generics.ListCreateAPIView):
#     queryset = Rate.objects.all()
#     serializer_class = RateSerializer


# class RateDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Rate.objects.all()
#     serializer_class = RateSerializer
