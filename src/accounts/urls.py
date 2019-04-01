from django.conf.urls import url, include
from .api_views import RegisterAPI, LoginAPI, GetUserAPI
from knox import views as knox_views


urlpatterns = [
    url(r'api/auth', include('knox.urls')),
    url(r'api/auth/register', RegisterAPI.as_view()),
    url(r'api/auth/login', LoginAPI.as_view()),
    url(r'api/auth/user', GetUserAPI.as_view()),
    url(r'api/auth/logout', knox_views.LoginView.as_view(), name='knox-logout')
]