import os
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core.mail import send_mail

from personal.models import ProjectItemModel
from personal.serializers import ProjectItemSerializer


class ProjectItemViewSet(viewsets.ModelViewSet):
    queryset = ProjectItemModel.objects.all()
    serializer_class = ProjectItemSerializer


@api_view(['POST'])
@authentication_classes([])
@permission_classes([AllowAny])
def contact_view(request):
    name = request.data.get('name')
    email = request.data.get('email')
    theme = request.data.get('theme')
    message = request.data.get('message')

    my_email = os.getenv("MY_EMAIL")
    host_user = os.getenv("EMAIL_HOST_USER")

    if not my_email:
        return Response(
            {"status": "error", "message": "Server configuration error."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    try:
        send_mail(
            subject=f"Portfolio: {theme} (from {name})",
            message=f"Contact Email: {email}\n\n{message}",
            from_email=host_user,
            recipient_list=[my_email],
            fail_silently=False,
        )
        return Response({"status": "success", "message": "Email sent!"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)