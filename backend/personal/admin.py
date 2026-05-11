import os

from django.core.mail import get_connection, EmailMessage
from django.contrib import admin

from personal.models import InboundMessageModel


@admin.register(InboundMessageModel)
class InboundMessageAdmin(admin.ModelAdmin):
    list_display = ('subject_email', 'subject_name', 'project_theme', 'created_at', 'is_read', 'is_deleted')
    list_filter = ('is_deleted', 'is_archived', 'is_read')

    def save_model(self, request, obj, form, change):
        reply = form.cleaned_data.get('reply_text')

        if reply:
            try:
                connection = get_connection(
                    backend=os.getenv("EMAIL_BACKEND"),
                    host=os.getenv('RESEND_EMAIL_HOST'),
                    port=os.getenv('EMAIL_PORT'),
                    username='resend',
                    password=os.getenv('RESEND_API_KEY'),
                    use_tls=os.getenv('RESEND_EMAIL_USE_TLS')
                )

                email = EmailMessage(
                    subject=f"Re: {obj.subject}",
                    body=reply,
                    from_email=os.getenv('RESEND_DEFAULT_EMAIL'),
                    to=[obj.email],
                    connection=connection,
                )

                email.send()
                self.message_user(request, "The reply has been successfully sent!")

            except Exception as e:
                self.message_user(request, f"Sending error: {e}", level='error')

        super().save_model(request, obj, form, change)