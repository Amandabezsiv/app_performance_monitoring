from django.contrib import admin
from .models import Alert

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('alert_type', 'severity', 'created_at', 'resolved')
    list_filter = ('alert_type', 'severity', 'resolved')
    search_fields = ('alert_message',)
