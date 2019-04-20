from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from ..serializers import ManufacturerSerializer
from ..models import Manufacturer


class GetManufacturerListView(generics.ListAPIView):

    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(Manufacturer.objects.all(),
                                         context=self.get_serializer_context(), many=True)

        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
