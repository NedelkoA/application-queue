from django.views.generic import TemplateView, UpdateView
from django.shortcuts import redirect, reverse, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

from users.models import Application
from myqueue.utils import get_connection
from .models import MyApplication, ChangeLog
from .utils.state import change_state


class GetRequestView(TemplateView, LoginRequiredMixin):
    template_name = 'operators/working_room.html'

    def get_context_data(self, **kwargs):
        connect = get_connection()
        context = super().get_context_data(**kwargs)
        context['all_items'] = connect.count_items
        return context

    def post(self, request):
        connect = get_connection()
        item = connect.pop()
        if item:
            app = Application.objects.get(id=item['id'])
            obj = change_state(app, 'review')
            if obj:
                obj.save()
                ChangeLog.objects.create(
                    operator=self.request.user,
                    application=obj,
                    updated_on=timezone.now(),
                    last_state='queue',
                    current_state=obj.status
                )
                MyApplication.objects.create(
                    operator=self.request.user,
                    application=obj
                )
                return redirect(reverse('request_info', kwargs={'pk': item['id']}))
        return render(request, self.template_name, context={'error': 'Queue is empty'})


class RequestInfo(UpdateView, LoginRequiredMixin):
    model = Application
    fields = (
        'status',
    )
    template_name = 'operators/request_info.html'

    def form_valid(self, form):
        obj = self.get_object()
        status = obj.status
        obj = change_state(obj, form.cleaned_data.get('status'))
        if obj:
            ChangeLog.objects.create(
                operator=self.request.user,
                application=obj,
                updated_on=timezone.now(),
                last_state=status,
                current_state=obj.status
            )
            return super().form_valid(form)
        form.add_error('status', 'This status not allowed')
        return render(
            self.request,
            self.template_name,
            context={
                'form': form,
                'object': self.get_object()
            }
        )

    def get_success_url(self):
        return reverse('request_info', kwargs={'pk': self.object.id})
