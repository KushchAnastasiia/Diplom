from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from ..serializers import GroupSerializer
from ..models import Group


class GetGroupListView(generics.ListAPIView):

    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(Group.objects.all(),
                                         context=self.get_serializer_context(), many=True)

        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
