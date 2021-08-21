from accounts.forms import SignUpForm
from accounts.models import User
from accounts.tokens import account_activation_token

from annoying.functions import get_object_or_None

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, RedirectView, UpdateView


class MyProfile(LoginRequiredMixin, UpdateView):
    queryset = User.objects.all()
    template_name = 'my-profile.html'
    success_url = reverse_lazy('index')
    fields = (
        'first_name',
        'last_name',
        'avatar',
        'phone',
        'email',
    )

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(pk=self.request.user.pk)
    #     return queryset

    def get_object(self, queryset=None):
        return self.request.user


class SingUp(CreateView):
    model = User
    template_name = 'signup.html'
    success_url = reverse_lazy('index')
    form_class = SignUpForm


class ActivateAccount(RedirectView):
    pattern_name = 'index'

    def get_redirect_url(self, *args, **kwargs):
        activation_key = kwargs.pop('username')
        activation_token = kwargs.pop('token')
        user = get_object_or_None(User.objects.only('is_active'), username=activation_key)

        """
        messages.debug(request, '%s SQL statements were executed.' % count)
        messages.info(request, 'Three credits remain in your account.')
        messages.success(request, 'Profile details updated.')
        messages.warning(request, 'Your account expires in three days.')
        messages.error(request, 'Document deleted.')
        """

        if user and account_activation_token.check_token(user, activation_token):
            if user.is_active:
                messages.warning(
                    self.request, 'Your account is already activated.')
            else:
                messages.info(
                    self.request, 'Thanks for activating your account.')
                user.is_active = True
                user.save(update_fields=('is_active', ))

        response = super().get_redirect_url(*args, **kwargs)
        return response
