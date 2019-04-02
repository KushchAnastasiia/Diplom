from django.conf.urls import url
from .api_views import SendMessageViewSet, AddFeaturedEquipmentView
from rest_framework import routers


urlpatterns = [
    url('api/send-message', SendMessageViewSet.as_view(), name='send-message')
]

router = routers.DefaultRouter()
router.register('api/add-featured', AddFeaturedEquipmentView, 'add-featured')

urlpatterns += router.urls
