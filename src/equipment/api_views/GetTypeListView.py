from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from ..serializers import TypeSerializer
from ..models import Type


class GetTypeListView(generics.ListAPIView):

    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TypeSerializer
    queryset = Type.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(Type.objects.all(),
                                         context=self.get_serializer_context(), many=True)

        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)

