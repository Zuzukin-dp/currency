# from annoying.functions import get_object_or_None

from currency.forms import ContactUsForm, RateForm, SourceForm
from currency.models import Analytics, ContactUs, Rate, Source
from currency.tasks import task_send_email
from currency.utils import generate_password as gp, read_txt

# from django.core.mail import send_mail
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView


def generate_pass(request):
    password = gp()
    return HttpResponse(password)


def index(request):
    return render(request, 'index.html')


def requirements(request):
    reader = read_txt('/home/bav/python/currency/requirements.txt')
    return HttpResponse(reader)


class AnalyticsView(ListView):
    queryset = Analytics.objects.all()
    template_name = 'analytics_list.html'


class RateListView(ListView):
    queryset = Rate.objects.all().select_related('bank')
    template_name = 'rate_list.html'


class RateDetailView(UserPassesTestMixin, DetailView):
    queryset = Rate.objects.all()
    template_name = 'rate_details.html'

    def test_func(self):
        return self.request.user.is_authenticated


class CreateRate(CreateView):
    model = Rate
    form_class = RateForm
    template_name = 'rate_create.html'
    success_url = reverse_lazy('index')


class RateUpdateView(UserPassesTestMixin, UpdateView):
    queryset = Rate.objects.all()
    form_class = RateForm
    template_name = 'rate_update.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        return self.request.user.is_superuser


class RateDeleteView(UserPassesTestMixin, DeleteView):
    queryset = Rate.objects.all()
    success_url = reverse_lazy('index')

    def test_func(self):
        return self.request.user.is_superuser


class SourceListView(ListView):
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


class ContactUsListView(ListView):
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

    def form_valid(self, form):
        data = form.cleaned_data
        body = f'''
        From: {data['email_from']}
        Topic: {data['subject']}
        Message
        {data['message']}
        '''

        task_send_email.delay(body)

        # from .tasks import print_hallo
        # print_hallo.delay()

        return super().form_valid(form)


class ContactUsUpdateView(UpdateView):
    queryset = ContactUs.objects.all()
    form_class = ContactUsForm
    template_name = 'contactus_update.html'
    success_url = reverse_lazy('index')


class ContactUsDeleteView(DeleteView):
    queryset = ContactUs.objects.all()
    success_url = reverse_lazy('index')


# class RateListApi(View):
#     def get(self, request):
#         rates = Rate.objects.all()
#         results = []
#         for rate in rates:
#             results.append({
#                 'id': rate.id,
#                 'sale': float(rate.sale),
#                 'buy': float(rate.buy),
#                 'bank': rate.bank_id,
#             })
#         import json
#         # return HttpResponse(json.dumps(results), content_type='application/json')
#         return JsonResponse(results, safe=False)
