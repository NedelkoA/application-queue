from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'make_request/$', views.MakeRequestView.as_view(), name='make_request'),
    url(r'requests_list/$', views.ApplicationListView.as_view(), name='requests_list'),
    url(r'request/(?P<pk>[0-9]+)/detail$', views.ApplicationDetailView.as_view(), name='request_detail'),
]
