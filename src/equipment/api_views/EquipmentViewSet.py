from rest_framework import generics, permissions, viewsets
from ..serializers import EquipmentSerializer
from helpers import CustomPaginator
from ..models import Equipment
from rest_framework.response import Response
from django.conf import settings


class EquipmentViewSet(viewsets.ModelViewSet):

    queryset = Equipment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EquipmentSerializer
    pagination_class = CustomPaginator

    def list(self, request, *args, **kwargs):
        queryset = self.paginate_queryset(
            queryset=Equipment.objects.all()
        )
        serialized_data = self.get_serializer(queryset, many=True)

        return Response({
            'data': serialized_data.data,
            'pagination': {
                'total_count': len(Equipment.objects.all()),
                'per_page': settings.EQ_PER_PAGE
            }
        })

    def retrieve(self, request, pk=None, *args, **kwargs):
        data = Equipment.objects.filter(id=int(pk))

        if data:
            serializer_data = self.get_serializer(data.first(), many=False)
            return Response({
                'data': serializer_data.data
            }, 200)
        else:
            return Response({
                'data': None
            })
