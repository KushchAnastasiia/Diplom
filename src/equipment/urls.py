from django.conf.urls import url
from rest_framework import routers

from .api_views import EquipmentViewSet


urlpatterns = [
    # url(r'^api/test-upload/$', TestViewSet.as_view(), 'api-upload')
]

router = routers.DefaultRouter()
router.register(r'api/equipment', EquipmentViewSet, 'api-equipment')

urlpatterns += router.urls
