import json
import os
import re
import traceback

import resend
from asgiref.sync import async_to_sync, sync_to_async
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes, authentication_classes, action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core.mail import send_mail, get_connection, EmailMessage
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from twisted.conch.client import default

from personal.models import ProjectItemModel, InboundMessageModel
from personal.serializers import ProjectItemSerializer, InboundMessageSerializer

resend.api_key = os.getenv("RESWND_RECIEVE_API_KEY")

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
    queryset = InboundMessageModel.objects.all().order_by('-created_at')
    serializer_class = InboundMessageSerializer

    pagination_class = None

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        if self.action == 'list':
            return InboundMessageModel.objects.filter(parent__isnull=True, is_deleted=False)
        return InboundMessageModel.objects.filter(is_deleted=False)

    def perform_create(self, serializer):
        is_admin = self.request.user.is_authenticated

        instance = serializer.save(is_from_admin=is_admin)

        if not is_admin:
            self._send_admin_notification(instance)

            self._send_auto_reply_to_client(instance)

    @action(
        detail=False,
        methods=['post'],
        url_path='sync',
        url_name='mail_sync',
        authentication_classes=[JWTAuthentication],
        permission_classes=[permissions.IsAuthenticated]
    )
    def sync_inbound_emails(self, request):
        try:
            resend_response = resend.Emails.Receiving.list()

            # Зчитуємо список на основі твого принту
            if isinstance(resend_response, dict):
                emails_list = resend_response.get('data', [])
            elif hasattr(resend_response, 'data'):
                emails_list = resend_response.data
            else:
                emails_list = resend_response or []

            new_messages_count = 0

            for brief_mail in emails_list:
                if not brief_mail or isinstance(brief_mail, str):
                    continue

                resend_id = getattr(brief_mail, 'id', None) or (
                    brief_mail.get('id') if isinstance(brief_mail, dict) else None)

                if not resend_id:
                    continue

                if InboundMessageModel.objects.filter(external_id=resend_id).exists():
                    continue

                try:
                    full_mail_response = resend.Emails.Receiving.get(email_id=resend_id)
                    # Приводимо до словника, якщо це об'єкт SDK
                    mail_dict = full_mail_response if isinstance(full_mail_response, dict) else getattr(
                        full_mail_response, '__dict__', {})
                except Exception as api_err:
                    print(f"Не вдалося завантажити повне тіло листа {resend_id}: {api_err}")
                    continue

                from_field = mail_dict.get('from', '') or getattr(full_mail_response, 'from', '')
                subject = mail_dict.get('subject', '(Без теми)') or getattr(full_mail_response, 'subject', '(Без теми)')

                mail_headers = mail_dict.get('headers', {}) or getattr(full_mail_response, 'headers', {})
                if not isinstance(mail_headers, dict):
                    mail_headers = {}

                text_content = mail_dict.get('text') or getattr(full_mail_response, 'text', None)
                html_content = mail_dict.get('html') or getattr(full_mail_response, 'html', None)

                if html_content and not text_content:
                    mail_body = re.sub(r'<[^>]+>', '', html_content).strip()
                else:
                    mail_body = text_content or html_content or '(Порожній лист)'

                def _parse_sender(from_string):
                    if not from_string:
                        return "Unknown", "unknown@example.com"
                    match = re.search(r'<(.*?)>', from_string)
                    if match:
                        name = from_string.split('<')[0].strip().strip('"') or "Unknown"
                        return name, match.group(1).strip()
                    return "Unknown", from_string.strip()

                sender_name, sender_email = _parse_sender(from_field)

                parent_message = None
                in_reply_to = mail_headers.get('In-Reply-To') or mail_headers.get('in-reply-to')

                if in_reply_to:
                    clean_id = in_reply_to.strip('<>')
                    parent_message = InboundMessageModel.objects.filter(
                        external_id__icontains=clean_id
                    ).first()

                if not parent_message and (subject.lower().startswith('re:') or subject.lower().startswith('fwd:')):
                    clean_subject = re.sub(r'^(re|fwd):\s*', '', subject, flags=re.IGNORECASE).strip()
                    parent_message = InboundMessageModel.objects.filter(
                        subject_email=sender_email,
                        project_theme__icontains=clean_subject
                    ).order_by('-created_at').first()

                InboundMessageModel.objects.create(
                    subject_name=sender_name,
                    subject_email=sender_email,
                    project_theme=subject,
                    mail_body=mail_body,
                    external_id=resend_id,
                    parent=parent_message,
                    is_from_admin=False,
                    is_read=False
                )

                if parent_message:
                    parent_message.is_replied = True
                    parent_message.save()

                new_messages_count += 1

            return Response({
                "success": True,
                "message": f"Sync has been completed. Count of new letters: {new_messages_count}"
            }, status=status.HTTP_200_OK)

        except Exception as e:
            traceback.print_exc()
            return Response({
                "error": "Resend API Sync Error",
                "details": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def _send_admin_notification(self, instance):
        my_email = os.getenv("MY_EMAIL")
        host_user = os.getenv("EMAIL_HOST_USER")

        if my_email and host_user:
            try:
                classical_smtp_connection = get_connection(
                    backend=os.getenv('EMAIL_BACKEND'),
                    host=os.getenv('EMAIL_HOST'),
                    port=int(os.getenv('EMAIL_PORT', 465)),
                    username=host_user,
                    password=os.getenv('EMAIL_HOST_PASSWORD'),
                    use_ssl=os.getenv('EMAIL_USE_SSL') == 'True' or os.getenv('EMAIL_USE_SSL') == True,
                    use_tls=os.getenv('EMAIL_USE_TLS') == 'True' or os.getenv('EMAIL_USE_TLS') == True,
                )

                send_mail(
                    subject=f"Portfolio: {instance.project_theme} (from {instance.subject_email})",
                    message=f"Subject: {instance.subject_name}\nContact Email: {instance.subject_email}\n\n{instance.mail_body}",
                    from_email=host_user,
                    recipient_list=[my_email],
                    connection=classical_smtp_connection,
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Ukr.net SMTP Error: {e}")

    def _send_auto_reply_to_client(self, instance):
        try:
            html_content = render_to_string('personal/emails/welcome.html', {
                'client_name': instance.subject_name,
                'project_theme': instance.project_theme
            })

            email = EmailMessage(
                subject=f"Thank you for your request! Тема: {instance.project_theme}",
                body=html_content,
                from_email=os.getenv('RESEND_DEFAULT_EMAIL'),
                to=[instance.subject_email],
            )
            email.content_subtype = "html"
            email.send()
        except Exception as e:
            print(f"Resend API Error (Auto-reply): {e}")

    # def perform_create(self, serializer):
    #     instance = serializer.save()

        # Telegram
        # send_telegram_notification(instance)

        # Brevo/Resend
        # if not instance.is_from_admin:
        #     send_auto_reply(instance.sender_email)

    @action(
        detail=False,
        methods=['post'],
        url_path='reply'
    )
    def reply(self, request):
        parent_id = request.data.get('parent_id')
        to_email = request.data.get('to_email')
        cc_email = request.data.get('cc_email')  # 🌟 Забираємо нове необов'язкове поле
        subject = request.data.get('subject')
        reply_body = request.data.get('body')

        if not all([parent_id, to_email, subject, reply_body]):
            return Response({"error": "Missing fields"}, status=status.HTTP_400_BAD_REQUEST)

        parent_message = get_object_or_404(InboundMessageModel, id=parent_id)

        try:
            headers = {}
            if parent_message.external_id:
                clean_msg_id = parent_message.external_id.strip('<>')
                headers = {
                    "In-Reply-To": f"<{clean_msg_id}>",
                    "References": f"<{clean_msg_id}>",
                }
            html_body = reply_body.replace('\n', '<br>')

            from_email = os.getenv('RESEND_DEFAULT_EMAIL') or "Admin <communicate@ychernyshev.dev>"

            params = {
                "from": from_email,
                "to": [to_email],
                "subject": subject if subject.lower().startswith('re:') else f"Re: {subject}",
                "html": f"<div>{html_body}</div>",
                "headers": headers
            }

            if cc_email and str(cc_email).strip():
                cc_list = [email.strip() for email in cc_email.split(",") if email.strip()]
                if cc_list:
                    params["cc"] = cc_list

            resend_response = resend.Emails.send(params)

            new_external_id = None
            if isinstance(resend_response, dict):
                new_external_id = resend_response.get('id')
            elif hasattr(resend_response, 'id'):
                new_external_id = resend_response.data.get('id') if isinstance(resend_response.data, dict) else getattr(
                    resend_response, 'id', None)

            parent_message.is_replied = True
            parent_message.save()

            InboundMessageModel.objects.create(
                parent=parent_message,
                subject_email=from_email,
                subject_name="Admin",
                project_theme=subject,
                mail_body=reply_body,
                external_id=new_external_id,
                is_from_admin=True,
                is_read=True
            )

            return Response({"success": True, "resend_id": new_external_id}, status=status.HTTP_201_CREATED)

        except Exception as e:
            traceback.print_exc()
            return Response({"error": "Failed to send reply via Resend API", "details": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        def _sync_email_pipeline():
            email = EmailMessage(
                subject=subject,
                body=reply_body,
                from_email=os.getenv('DEFAULT_FROM_EMAIL'),
                to=[to_email],
            )
            email.send()

            parent_message.is_replead = True
            parent_message.save()

            InboundMessageModel.objects.create(
                parent=parent_message,
                subject_email=os.getenv('DEFAULT_FROM_EMAIL'),
                subject_name="Admin",
                project_theme=subject,
                mail_body=reply_body,
                is_from_admin=True,
                is_read=True
            )

        try:
            sync_to_async(_sync_email_pipeline, thread_sensitive=False)()
            return Response({"success": True}, status=status.HTTP_201_CREATED)

        except Exception as e:
            traceback.print_exc()
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Inbound messages
    @action(
        detail=False,
        methods=['post'],
        url_path='webhook',
        permission_classes=[permissions.AllowAny],
        authentication_classes=[]
    )
    def resend_webhook(self, request):
        try:
            data = request.data

            email_id = data.get('email_id') or data.get('id')
            if email_id and InboundMessageModel.objects.filter(external_id=email_id).exists():
                return Response({'status': 'ignored', 'message': 'Duplicate webhook'}, status=status.HTTP_200_OK)

            def _parse_sender(from_string):
                if not from_string: return "Unknown", "unknown@example.com"
                match = re.search(r'<(.*?)>', from_string)
                if match:
                    return from_string.split('<')[0].strip().strip('"') or "Unknown", match.group(1).strip()
                return "Unknown", from_string.strip()

            from_field = data.get('from', '')
            sender_name, sender_email = _parse_sender(from_field)

            subject = data.get('subject', '(Без теми)')
            body = data.get('text') or data.get('html') or ''

            parent_message = None
            headers = data.get('headers', {})
            in_reply_to = headers.get('In-Reply-To') or headers.get('in-reply-to')
            if in_reply_to:
                parent_message = InboundMessageModel.objects.filter(external_id=in_reply_to).first()

            InboundMessageModel.objects.create(
                subject_name=sender_name,
                subject_email=sender_email,
                project_theme=subject,
                mail_body=body,
                external_id=email_id,
                parent=parent_message,
                is_from_admin=False,
                is_read=False
            )

            return Response({'status': 'delivered'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class SetMessageStatusViewSet(viewsets.ModelViewSet):
    queryset = InboundMessageModel.objects.all()
    serializer_class = InboundMessageSerializer

    @action(
        detail=True,
        methods=['patch'],
        url_path='is_read',
        permission_classes=[permissions.AllowAny],  # Потім зміни на IsAuthenticated, коли протестуєш
        authentication_classes=[]
    )
    def is_read(self, request, pk=None):
        message = self.get_object()

        is_read_status = request.data.get('is_read', False)

        message.is_read = is_read_status
        message.save()

        return Response({
            "success": True,
            "message_id": message.id,
            "is_read": message.is_read
        }, status=status.HTTP_200_OK)