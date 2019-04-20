from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from ..serializers import ManufacturerSerializer, CountrySerializer
from ..models import Manufacturer, Country


class GetManufacturerListView(generics.ListAPIView):

    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(Manufacturer.objects.all(),
                                         context=self.get_serializer_context(), many=True).data

        for x in serializer:
            country = CountrySerializer(
                Country.objects.filter(id=int(x["country"])).first()
            ).data

            x['country'] = country

        return Response({
            "data": serializer
        }, status=status.HTTP_200_OK)
