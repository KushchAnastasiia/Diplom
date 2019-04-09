from django.conf.urls import url
from .views import display


urlpatterns = [
    url(r'^$', display, name='swagger-main'),
]