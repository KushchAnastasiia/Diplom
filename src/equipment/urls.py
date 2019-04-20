from django.conf.urls import url
from rest_framework import routers

from .api_views import *


urlpatterns = [
    url(r'^api/countries/$', GetCountryListView.as_view()),
    url(r'^api/types/$', GetTypeListView.as_view()),
    url(r'^api/groups/$', GetGroupListView.as_view()),
    url(r'^api/subgroups/$', GetSubgroupListView.as_view()),
    url(r'^api/manufacturers/$', GetManufacturerListView.as_view()),
    url(r'^api/markets/$', GetMarketListView.as_view()),
]

router = routers.DefaultRouter()
router.register(r'api/equipment', EquipmentViewSet, 'api-equipment')

urlpatterns += router.urls
