from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from ..tasks import add_to_featured
from rest_framework import status
from personal_area.serializers import FeaturedEquipmentSerializer
from personal_area.models import FeaturedEquipment
from equipment.models import Equipment
from equipment.serializers import EquipmentSerializer
from helpers import get_full_equipment_data
from django.conf import settings


class AddFeaturedEquipmentView(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = FeaturedEquipmentSerializer
    queryset = FeaturedEquipment.objects.all()

    def update(self, request, *args, **kwargs):
        return Response({
            'data': {},
            'errors': {
                'message': 'Have no access to update!',
            }
        }, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def list(self, request, *args, **kwargs):
        if request.user:
            featured_list = FeaturedEquipment.objects.filter(user_id=request.user.id)
            featured_count = len(FeaturedEquipment.objects.filter(
                user_id=request.user.id).all())

            featured_data = []

            for x in featured_list:
                featured_data.append(Equipment.objects.filter(id=x.equipment_id).first())

            featured_serializer = EquipmentSerializer(
                featured_data,
                context=self.get_serializer_context(), many=True).data

            featured_serializer = [get_full_equipment_data(x) for x in featured_serializer]

            return Response({
                'data': {
                    'current_count': featured_count,
                    'featured': featured_serializer,
                }
            }, status=status.HTTP_202_ACCEPTED)
        return Response({
            'data': {
                'featured': [],
            },
            'errors': {
                'message': 'No user token found!'
            }
        }, status=status.HTTP_401_UNAUTHORIZED)

    def retrieve(self, request, pk=None, *args, **kwargs):
        if request.user and pk:
            featured = FeaturedEquipment.objects.filter(
                user_id=request.user.id, equipment_id=pk).first()

            featured_serializer = EquipmentSerializer(
                Equipment.objects.filter(id=featured.equipment_id).first(),
                context=self.get_serializer_context(), many=False).data

            return Response({
                'data': get_full_equipment_data(featured_serializer)
            }, status=status.HTTP_202_ACCEPTED)

        return Response({
            'data': {
                'featured': [],
            },
            'errors': {
                'message': 'No user token found!'
            }
        }, status=status.HTTP_401_UNAUTHORIZED)

    def create(self, request, *args, **kwargs):
        featured = len(FeaturedEquipment.objects.filter(
            user_id=request.user.id).all())

        if featured < settings.USER_FEATURED_COUNT:
            data = request.data
            data['user_id'] = request.user.id
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            add_to_featured(serializer=serializer)
            headers = self.get_success_headers(serializer.data)

            return Response({
                'data': {
                    'current_count': featured + 1,
                    'total_count': settings.USER_FEATURED_COUNT,
                    'feature': serializer.data,
                }
            }, status=status.HTTP_201_CREATED, headers=headers)

        return Response({
            'data': {},
            'errors': {
                'message': 'Message limit was exceeded!'
            }
        }, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()

        return Response({
            'data': {
                'message': 'Feature removed!'
            }
        }, status=status.HTTP_204_NO_CONTENT)
