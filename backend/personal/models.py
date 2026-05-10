from django.db import models

class ProjectItemModel(models.Model):
    title = models.CharField(max_length=35)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    source_code = models.TextField()
    live_preview = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'project item'
        verbose_name_plural = "Project Items"


class ContactMessageModel(models.Model):
    subject_name = models.CharField(max_length=100, blank=True)
    subject_email = models.EmailField()
    project_theme = models.CharField(max_length=255)
    mail_body = models.TextField()
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies'
    )
    is_from_admin = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
        verbose_name="contact message"
        verbose_name_plural="Contact Messages"

    def __str__(self):
        return f"{'Admin' if self.is_from_admin else self.sender_email}: {self.subject[:30]}"
