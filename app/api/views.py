# from rest_framework import generics
from currency.models import Rate
from currency import choices
from api.serializers import RateSerializer, RateDetailsSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from api.pagination import RatePagination


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    # serializer_class = RateSerializer
    pagination_class = RatePagination

    def get_serializer_class(self):
        if 'pk' in self.kwargs:
            return RateDetailsSerializer
        return RateSerializer


def get(request, format=None):

    return Response(choices.RATE_TYPE_CHOICES)


class RateTypeChoiceView(APIView):
    pass

# class RateList(generics.ListCreateAPIView):
#     queryset = Rate.objects.all()
#     serializer_class = RateSerializer


# class RateDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Rate.objects.all()
#     serializer_class = RateSerializer
