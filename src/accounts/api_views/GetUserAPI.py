from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from ..serializers import UserSerializer, LoginSerializer


class GetUserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
