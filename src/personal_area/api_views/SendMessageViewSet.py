from rest_framework import generics, permissions, views
from rest_framework.response import Response
from ..tasks import send_message


class SendMessageViewSet(generics.GenericAPIView):

    permission_classes = [
        permissions.AllowAny
    ]

    def post(self, request, *args, **kwargs):
        send_message.delay(
            request.data.get('title', ""),
            request.data.get('description', ''))

        return Response({
            "data": {
                "message": "Message is sending!"
            }
        }, 200)
