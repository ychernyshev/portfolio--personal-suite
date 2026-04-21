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
