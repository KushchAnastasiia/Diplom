from rest_framework import generics, permissions
from rest_framework.response import Response


class TestViewSet(generics.GenericAPIView):

    # serializer_class = RegisterSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def post(self, request, *a, **k):

        return Response({
            "data": {
                "file": request.data['file']
            }
        })