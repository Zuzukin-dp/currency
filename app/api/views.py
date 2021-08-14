from api.filters import ContactUsFilter, RateFilter
from api.pagination import ContactUsPagination, RatePagination
from api.serializers import \
    ContactUsSendMailSerializer, ContactUsSerializer, \
    RateDetailsSerializer, RateSerializer, \
    SourceDetailsSerializer, SourceSerializer
from api.throttles import AnonUserRateThrottle

from currency import choices
from currency.models import ContactUs, Rate, Source

from django.shortcuts import render

from django_filters import rest_framework as filters

from rest_framework import filters as rest_framework_filters
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework import generics


def api_list_page(request):
    return render(request, 'api_list.html')


class SourceListView(viewsets.ModelViewSet):
    queryset = Source.objects.all().order_by('created')
    # serializer_class = SourceDetailsSerializer

    def get_serializer_class(self):
        if 'pk' in self.kwargs:
            # queryset = Source.objects.all().prefetch_related('rates_set')
            # breakpoint()
            return SourceDetailsSerializer
        return SourceSerializer


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


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all().order_by('-created')
    pagination_class = ContactUsPagination
    # serializer_class = ContactUsSerializer
    throttle_classes = [AnonUserRateThrottle]
    filterset_class = ContactUsFilter
    filter_backends = (filters.DjangoFilterBackend,
                       rest_framework_filters.OrderingFilter,
                       rest_framework_filters.SearchFilter,
                       )
    ordering_fields = ['id', 'email_from', 'subject', 'message', 'created']
    search_fields = ['id', 'email_from', 'subject', 'message', 'created']

    def get_serializer_class(self):
        # breakpoint()
        if 'create' in self.action:
            return ContactUsSendMailSerializer
        return ContactUsSerializer


class RateTypeChoiceView(APIView):
    def get(self, request, format=None):  # noqa
        return Response(choices.RATE_TYPE_CHOICES)


# class RateList(generics.ListCreateAPIView):
#     queryset = Rate.objects.all()
#     serializer_class = RateSerializer


# class RateDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Rate.objects.all()
#     serializer_class = RateSerializer
