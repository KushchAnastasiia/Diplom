from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from ..serializers import CountrySerializer
from ..models import Country


class GetCountryListView(generics.ListAPIView):

    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CountrySerializer
    queryset = Country.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
