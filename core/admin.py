from django.contrib import admin
from .models import AuditLog

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'model_name', 'timestamp', 'ip_address')
    search_fields = ('user__username', 'action', 'model_name')
    list_filter = ('action', 'model_name', 'timestamp')
    readonly_fields = ('timestamp',)
