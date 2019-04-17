from rest_framework import generics, permissions, viewsets
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from ..serializers import *
from helpers import CustomPaginator
from ..models import *
from rest_framework.response import Response
from django.conf import settings
from helpers import get_full_equipment_data


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class EquipmentViewSet(viewsets.ModelViewSet):

    queryset = Equipment.objects.all()
    permission_classes = [
        permissions.IsAdminUser | ReadOnly,
    ]
    serializer_class = EquipmentSerializer
    pagination_class = CustomPaginator

    def list(self, request, *args, **kwargs):
        queryset = self.paginate_queryset(
            queryset=Equipment.objects.all()
        )
        serialized_data = self.get_serializer(queryset, many=True).data

        eq_full_data = []
        for x in serialized_data:
            eq_full_data.append(get_full_equipment_data(x))
        
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
                'data': get_full_equipment_data(serializer_data)
            }, 200)
        else:
            return Response({
                'data': None
            })
