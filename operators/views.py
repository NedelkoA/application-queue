import logging

from django.views.generic import TemplateView, UpdateView
from django.shortcuts import redirect, reverse, render
from django.contrib.auth.mixins import LoginRequiredMixin

from users.models import Application
from myqueue.utils import get_connection
from .models import MyApplication
from .utils.state import change_state

logger = logging.getLogger('state_info')


class GetRequestView(TemplateView, LoginRequiredMixin):
    template_name = 'operators/working_room.html'

    def get_context_data(self, **kwargs):
        connect = get_connection()
        context = super().get_context_data(**kwargs)
        context['all_items'] = connect.connection.llen('item_list')
        return context

    def post(self, request):
        if request.method == "POST":
            connect = get_connection()
            item = connect.pop()
            if item:
                app = Application.objects.get(id=item['id'])
                obj = change_state(app, 'review')
                if obj:
                    logger.info(
                        'User ' + str(self.request.user) +
                        ' took application #' + str(obj.id) +
                        ' from queue and set status \'' + str(obj.status) + '\''
                    )
                    obj.save()
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
            logger.info(
                'User ' + str(self.request.user) +
                ' change status from \'' + status +
                '\' to \'' + obj.status +
                '\' for application #' + str(obj.id)
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
