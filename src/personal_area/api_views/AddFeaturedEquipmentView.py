from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from ..tasks import add_to_featured
from ..serializers import FeaturedEquipmentSerializer
from rest_framework import status


class AddFeaturedEquipmentView(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = FeaturedEquipmentSerializer

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

    @action(methods=['post', 'put', 'patch'], detail=True, permission_classes=[permissions.IsAdminUser])
    def update(self, request, *args, **kwargs):
        super(AddFeaturedEquipmentView, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response({
            'data': {
                'message': 'Feature removed!'
            }
        }, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['get'], detail=True, permission_classes=[permissions.IsAdminUser])
    def retrieve(self, request, *args, **kwargs):
        super(AddFeaturedEquipmentView, self).retrieve(request, *args, **kwargs)

    @action(methods=['get', 'post'], detail=True, permission_classes=[permissions.IsAdminUser])
    def list(self, request, *args, **kwargs):
        super(AddFeaturedEquipmentView, self).list(request, *args, **kwargs)

    # def post(self, request, *a, **k):
    #     add_to_featured(request.data.get('user_id', None), request.data.get('equipment_id', None))
    #
    #     return Response({
    #         'data': {
    #             'message': 'Added favourites'
    #         }
    #     }, 200)
