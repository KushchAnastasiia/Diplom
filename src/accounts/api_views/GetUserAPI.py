from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from ..serializers import UserSerializer, LoginSerializer
from personal_area.serializers import FeaturedEquipmentSerializer
from personal_area.models import FeaturedEquipment


class GetUserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        featured_list = FeaturedEquipment.objects.filter(user_id=instance.id)
        featured_serializer = FeaturedEquipmentSerializer(featured_list, many=True)
        return Response({
            'data': {
                'user': serializer.data,
                'featured': featured_serializer.data
            }
        }, status=status.HTTP_202_ACCEPTED)

    def get_object(self):
        return self.request.user
