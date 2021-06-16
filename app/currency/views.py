from annoying.functions import get_object_or_None

from currency.forms import ContactUsForm, RateForm, SourceForm
from currency.models import ContactUs, Rate, Source
from currency.utils import generate_password as gp, read_txt

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView,DeleteView
from django.urls import reverse_lazy


def generate_pass(request):
    password = gp()
    return HttpResponse(password)


def index(request):
    return render(request, 'index.html')


def requirements(request):
    reader = read_txt('/home/bav/python/currency/requirements.txt')
    return HttpResponse(reader)


class RateLitView(ListView):
    queryset = Rate.objects.all()
    template_name = 'rate_list.html'


class RateDetailView(DetailView):
    queryset = Rate.objects.all()
    template_name = 'rate_details.html'


class CreateRate(CreateView):
    model = Rate
    form_class = RateForm
    template_name = 'rate_create.html'
    success_url = reverse_lazy('index')


class RateUpdateView(UpdateView):
    queryset = Rate.objects.all()
    form_class = RateForm
    template_name = 'rate_update.html'
    success_url = reverse_lazy('index')


class RateDeleteView(DeleteView):
    queryset = Rate.objects.all()
    success_url = reverse_lazy('index')


class SourceLitView(ListView):
    queryset = Source.objects.all()
    template_name = 'source_list.html'


class SourceDetailView(DetailView):
    queryset = Source.objects.all()
    template_name = 'source_details.html'


class CreateSource(CreateView):
    model = Source
    form_class = SourceForm
    template_name = 'source_create.html'
    success_url = reverse_lazy('index')


class SourceUpdateView(UpdateView):
    queryset = Source.objects.all()
    form_class = SourceForm
    template_name = 'source_update.html'
    success_url = reverse_lazy('index')


class SourceDeleteView(DeleteView):
    queryset = Source.objects.all()
    success_url = reverse_lazy('index')


class ContactUsLitView(ListView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus_list.html'


class ContactUsDetailView(DetailView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus_details.html'


class CreateContactUs(CreateView):
    # queryset = ContactUs.objects.all()
    model = ContactUs
    form_class = ContactUsForm
    template_name = 'contactus_create.html'
    success_url = reverse_lazy('index')


class ContactUsUpdateView(UpdateView):
    queryset = ContactUs.objects.all()
    form_class = ContactUsForm
    template_name = 'contactus_update.html'
    success_url = reverse_lazy('index')


class ContactUsDeleteView(DeleteView):
    queryset = ContactUs.objects.all()
    success_url = reverse_lazy('index')
