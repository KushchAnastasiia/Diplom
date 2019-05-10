from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from ..serializers import SubGroupSerializer, GroupSerializer
from ..models import SubGroup, Group


class GetSubgroupListView(generics.ListAPIView):

    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SubGroupSerializer
    queryset = SubGroup.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(SubGroup.objects.all(),
                                         context=self.get_serializer_context(), many=True).data

        for x in serializer:
            country = GroupSerializer(
                Group.objects.filter(id=int(x["group"])).first()
            ).data

            x['group'] = country

        return Response({
            "data": serializer
        }, status=status.HTTP_200_OK)
