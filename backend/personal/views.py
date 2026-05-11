import os
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes, authentication_classes, action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from personal.models import ProjectItemModel, ContactMessageModel
from personal.serializers import ProjectItemSerializer, ContactMessageSerializer


@action(detail=True, methods=['post'])
def mark_as_read(self, request, pk=None):
    message = self.get_object()
    message.is_read = True
    message.save()
    return Response({'status': 'marked as read'})


class ProjectItemViewSet(viewsets.ModelViewSet):
    queryset = ProjectItemModel.objects.all()
    serializer_class = ProjectItemSerializer

# =====
# THE LEGACY CODE FOR JOB TO MAIL SEND ONLY
# =====

# @api_view(['POST'])
# @authentication_classes([])
# @permission_classes([AllowAny])
# def contact_view(request):
#     name = request.data.get('name')
#     email = request.data.get('email')
#     theme = request.data.get('theme')
#     message = request.data.get('message')
#
#     my_email = os.getenv("MY_EMAIL")
#     host_user = os.getenv("EMAIL_HOST_USER")
#
#     if not my_email:
#         return Response(
#             {"status": "error", "message": "Server configuration error."},
#             status=status.HTTP_500_INTERNAL_SERVER_ERROR
#         )
#
#     try:
#         send_mail(
#             subject=f"Portfolio: {theme} (from {name})",
#             message=f"Contact Email: {email}\n\n{message}",
#             from_email=host_user,
#             recipient_list=[my_email],
#             fail_silently=False,
#         )
#         return Response({"status": "success", "message": "Email sent!"}, status=status.HTTP_200_OK)
#     except Exception as e:
#         return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# =====
# THE NEWEST CODE TO EMAIL THE POST SERVICE AND SAVE AN EMAIL TO THE DATABASE
# =====

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessageModel.objects.all().order_by('-created_at')
    serializer_class = ContactMessageSerializer

    pagination_class = None

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        if self.action == 'list':
            return ContactMessageModel.objects.filter(parent__isnull=True, is_deleted=False)
        return ContactMessageModel.objects.filter(is_deleted=False)

    def perform_create(self, serializer):
        is_admin = self.request.user.is_authenticated

        instance = serializer.save(is_from_admin=is_admin)

        if not is_admin:
            self._send_standard_email(instance)

    def _send_standard_email(self, instance):
        my_email = os.getenv("MY_EMAIL")
        host_user = os.getenv("EMAIL_HOST_USER")

        if my_email and host_user:
            try:
                send_mail(
                    subject=f"Portfolio: {instance.project_theme} (from {instance.subject_email})",
                    message=f"Subject: {instance.subject_name}\nContact Email: {instance.subject_email}\n\n{instance.mail_body}",
                    from_email=host_user,
                    recipient_list=[my_email],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Legacy SMTP Error: {e}")

    # def perform_create(self, serializer):
    #     instance = serializer.save()

        # Telegram
        # send_telegram_notification(instance)

        # Brevo/Resend
        # if not instance.is_from_admin:
        #     send_auto_reply(instance.sender_email)