from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'room/$', views.GetRequestView.as_view(), name='get_request'),
    url(r'request/(?P<pk>[0-9]+)/detail$', views.RequestInfo.as_view(), name='request_info'),
]
