from currency.forms import RateForm, SourceForm
from currency.models import Rate, Source
from currency.utils import generate_password as gp, read_txt

from annoying.functions import get_object_or_None
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render


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


def rate_create(request):
    if request.method == 'POST':
        form_data = request.POST
        form = RateForm(form_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/currency/rate/list/')
    elif request.method == 'GET':
        form = RateForm()

    context = {
        'form': form,
        'count': Rate.objects.count()
    }
    return render(request, 'rate_create.html', context=context)


def rate_update(request, pk):
    instance = get_object_or_404(Rate, id=pk)

    if request.method == 'POST':
        form_data = request.POST
        form = RateForm(form_data, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/currency/rate/list/')
    elif request.method == 'GET':
        form = RateForm(instance=instance)

    context = {
        'form': form,
    }
    return render(request, 'rate_update.html', context=context)


def rate_delete(request, pk):
    instance = get_object_or_None(Rate, id=pk)
    if instance is not None:
        instance.delete()
    return HttpResponseRedirect('/currency/rate/list/')


def source_list(request):
    queryset = Source.objects.all()
    # print(queryset.query)

    context = {
        'object': queryset,
    }
    return render(request, 'source_list.html', context=context)


def source_details(request, pk):
    source = get_object_or_404(Source, id=pk)

    context = {
        'object': source,
    }
    return render(request, 'source_details.html', context=context)


def source_create(request):
    if request.method == 'POST':
        form_data = request.POST
        form = SourceForm(form_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/currency/source/list/')
    elif request.method == 'GET':
        form = SourceForm()

    context = {
        'form': form,
        'count': Source.objects.count()
    }
    return render(request, 'source_create.html', context=context)


def source_update(request, pk):
    instance = get_object_or_404(Source, id=pk)

    if request.method == 'POST':
        form_data = request.POST
        form = SourceForm(form_data, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/currency/source/list/')
    elif request.method == 'GET':
        form = SourceForm(instance=instance)

    context = {
        'form': form,
    }
    return render(request, 'source_update.html', context=context)


def source_delete(request, pk):
    instance = get_object_or_None(Source, id=pk)
    if instance is not None:
        instance.delete()
    return HttpResponseRedirect('/currency/source/list/')
