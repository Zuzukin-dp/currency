from django.shortcuts import render, get_object_or_404
from currency.models import Rate
from currency.utils import generate_password as gp, read_txt

from django.http import HttpResponse


def generate_pass(request):
    password = gp()
    return HttpResponse(password)


def requirements(request):
    reader = read_txt('/home/bav/python/currency/requirements.txt')
    return HttpResponse(reader)


def rate_list(request):
    queryset = Rate.objects.all()
    # print(queryset.query)

    context = {
        'object': queryset,
    }
    return render(request, 'rate_list.html', context=context)


def rate_details(request, pk):
    rate = get_object_or_404(Rate, id=pk)

    context = {
        'object': rate,
    }
    return render(request, 'rate_details.html', context=context)
