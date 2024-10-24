from django.db import models

class Alert(models.Model):
    ALERT_TYPES = [
        ('CPU', 'CPU Usage High'),
        ('MEMORY', 'Memory Usage High'),
        ('DISK', 'Disk Space Low'),
        ('LATENCY', 'High Latency'),
    ]

    SEVERITY_LEVELS = [
        ('CRITICAL', 'Critical'),
        ('WARNING', 'Warning'),
        ('INFO', 'Info'),
    ]

    alert_type = models.CharField(max_length=10, choices=ALERT_TYPES)
    severity = models.CharField(max_length=10, choices=SEVERITY_LEVELS)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)

   
    def __str__(self):
        # Define the alert message template
        return f"{self.get_alert_type_display()} - {self.get_severity_display()}"

    def resolve_alert(self):
        # Mark the alert as resolved
        self.resolved = True
        self.save()
