from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from ..tasks import add_to_featured
from ..serializers import FeaturedEquipmentSerializer
from ..models import FeaturedEquipment
from rest_framework import status


class AddFeaturedEquipmentView(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = FeaturedEquipmentSerializer
    queryset = FeaturedEquipment.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        add_to_featured(serializer=serializer)
        headers = self.get_success_headers(serializer.data)

        return Response({
            'data': {
                'feature': serializer.data,
            }
        }, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()

        return Response({
            'data': {
                'message': 'Feature removed!'
            }
        }, status=status.HTTP_204_NO_CONTENT)
