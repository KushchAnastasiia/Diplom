from django.conf.urls import url
from rest_framework import routers

from .api_views import EquipmentViewSet, GetCountryListView


urlpatterns = [
    url(r'^api/countries/$', GetCountryListView.as_view(), 'get-countries')
]

router = routers.DefaultRouter()
router.register(r'api/equipment', EquipmentViewSet, 'api-equipment')

urlpatterns += router.urls
