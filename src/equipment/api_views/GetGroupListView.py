from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from ..serializers import GroupSerializer, SubGroupSerializer
from ..models import Group, SubGroup


class GetGroupListView(generics.ListAPIView):

    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

    def list(self, request, *args, **kwargs):
        groups = self.get_serializer(Group.objects.all(),
                                         context=self.get_serializer_context(), many=True).data
        for x in groups:
            x['subgroups'] = SubGroupSerializer(
                SubGroup.objects.filter(group=x['id']), many=True
            ).data
        return Response({
            "data": groups
        }, status=status.HTTP_200_OK)
