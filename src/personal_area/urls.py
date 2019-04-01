from django.conf.urls import url
from .api_views import SendMessageViewSet


urlpatterns = [
    url('api/send-message', SendMessageViewSet.as_view(), name='send-message')
]
