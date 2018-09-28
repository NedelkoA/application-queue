from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Application
from myqueue.utils import get_connection


class MakeRequestView(CreateView, LoginRequiredMixin):
    model = Application
    fields = (
        'phone_number',
        'email',
        'text',
    )
    template_name = 'users/application.html'
    success_url = reverse_lazy('requests_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        obj = form.save()
        valid = super().form_valid(form)
        obj.__dict__.pop('_state', None)
        obj.__dict__.pop('updated_on', None)
        connect = get_connection()
        connect.push(**obj.__dict__)
        return valid


class ApplicationListView(ListView, LoginRequiredMixin):
    model = Application
    template_name = 'users/application_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Application.objects.filter(
            user=self.request.user
        ).exclude(status__in=['success', 'unsuccess']).order_by('-updated_on')
        context['successed_list'] = Application.objects.filter(
            user=self.request.user,
            status__in=['success', 'unsuccess']
        )
        return context


class ApplicationDetailView(DetailView):
    model = Application
    template_name = 'users/application_detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(
            Application,
            pk=self.kwargs['pk'],
            user=self.request.user
        )
