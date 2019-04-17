from django.contrib import admin
from .models import *


admin.site.register(Equipment)
admin.site.register(Manufacturer)
admin.site.register(Country)
admin.site.register(Type)
admin.site.register(Group)
admin.site.register(SubGroup)
admin.site.register(EquipmentMarketConnection)
admin.site.register(Market)

admin.site.site_title = "Med api admin panel"
admin.site.site_header = "Med api admin panel"
admin.site.gettext_lazy = "Med api admin panel"
