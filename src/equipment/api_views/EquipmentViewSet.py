from rest_framework import generics, permissions, viewsets
from ..serializers import *
from helpers import CustomPaginator
from ..models import *
from rest_framework.response import Response
from django.conf import settings


class EquipmentViewSet(viewsets.ModelViewSet):

    queryset = Equipment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EquipmentSerializer
    pagination_class = CustomPaginator

    def get_full_data(self, d):
        ctx = d

        type_of = TypeSerializer(
            Type.objects.filter(id=int(d["type_of"])).first()).data
        
        manufacture = ManufacturerSerializer(
            Manufacturer.objects.filter(id=int(d["manufacture"])).first()).data
        
        subgroup = SubGroupSerializer(
            SubGroup.objects.filter(id=int(d["subgroup"])).first()).data
        
        group = GroupSerializer(
            Group.objects.filter(id=int(subgroup["id"])).first()).data
        
        ctx['type_of'] = type_of
        ctx['manufacture'] = manufacture
        ctx['subgroup'] = subgroup
        ctx['group'] = group
        
        return ctx

    def list(self, request, *args, **kwargs):
        queryset = self.paginate_queryset(
            queryset=Equipment.objects.all()
        )
        serialized_data = self.get_serializer(queryset, many=True).data

        eq_full_data = []
        for x in serialized_data:
            eq_full_data.append(self.get_full_data(x))
        
        return Response({
            'data': eq_full_data,
            'pagination': {
                'total_count': len(Equipment.objects.all()),
                'per_page': settings.EQ_PER_PAGE
            }
        })

    def retrieve(self, request, pk=None, *args, **kwargs):
        data = Equipment.objects.filter(id=int(pk))

        if data:
            serializer_data = self.get_serializer(data.first(), many=False).data
            return Response({
                'data': self.get_full_data(serializer_data)
            }, 200)
        else:
            return Response({
                'data': None
            })
