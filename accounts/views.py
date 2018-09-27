from django.shortcuts import redirect, reverse
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView, UpdateView, TemplateView
from django.urls import reverse_lazy

from .forms import RegistrationForm


class RegistrationView(CreateView):
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('index')
    form_class = RegistrationForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('index'))
        return super().get(request, args, kwargs)

    def form_valid(self, form):
        valid = super().form_valid(form)
        user = authenticate(
            username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password1')
        )
        login(self.request, user)
        return valid


class IndexView(TemplateView):
    template_name = 'accounts/index.html'

