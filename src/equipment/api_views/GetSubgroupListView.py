from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from ..serializers import SubGroupSerializer
from ..models import SubGroup


class GetSubgroupListView(generics.ListAPIView):

    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SubGroupSerializer
    queryset = SubGroup.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(SubGroup.objects.all(),
                                         context=self.get_serializer_context(), many=True)

        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)

