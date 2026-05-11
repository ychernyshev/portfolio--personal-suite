from django.contrib import admin

from personal.models import InboundMessageModel


# Register your models here.
@admin.register(InboundMessageModel)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('subject_email', 'subject_name', 'project_theme', 'created_at', 'is_read', 'is_deleted')
    list_filter = ('is_deleted', 'is_archived', 'is_read')