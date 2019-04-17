from django.conf.urls import url, include
from .api_views import RegisterAPI, LoginAPI, GetUserAPI, LogoutAPIView
from knox import views as knox_views


urlpatterns = [
    url(r'api/auth/register/', RegisterAPI.as_view()),
    url(r'api/auth/login/', LoginAPI.as_view()),
    url(r'api/auth/logout/', LogoutAPIView.as_view(), name='knox-logout'),
    url(r'api/auth', include('knox.urls')),
    url(r'api/auth/user/', GetUserAPI.as_view()),
]
