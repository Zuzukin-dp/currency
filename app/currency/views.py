from currency.models import Rate
from currency.utils import generate_password as gp, read_txt

from django.http import HttpResponse
# from django.shortcuts import render


def generate_pass(request):
    password = gp()
    return HttpResponse(password)


def requirements(request):
    reader = read_txt('/home/bav/python/currency/requirements.txt')
    return HttpResponse(reader)


def rate_list(request):
    queryset = Rate.objects.all()
    ids = []
    for rate in queryset:
        ids.append(rate.id)
    return HttpResponse(str(ids))
