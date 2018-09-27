from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    url(r'registration/$', views.RegistrationView.as_view(), name='registration'),
    url(r'logout/$', LogoutView.as_view(next_page='login'), name='logout'),
    url(r'login/$', LoginView.as_view(
        template_name='accounts/login.html',
        redirect_authenticated_user=True,
    ), name='login'),
    url(r'index/$', views.IndexView.as_view(), name='index'),
]
