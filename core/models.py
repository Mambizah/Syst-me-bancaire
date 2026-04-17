from django.db import models
from django.conf import settings
from django.utils import timezone

class AuditLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=255)
    model_name = models.CharField(max_length=100)
    object_id = models.PositiveIntegerField()
    details = models.TextField(blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.action} - {self.timestamp}"
