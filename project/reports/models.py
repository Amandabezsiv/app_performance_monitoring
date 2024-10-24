from django.db import models

class Report(models.Model):
    title = models.CharField(max_length=255)
    generated_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()  

    def __str__(self):
        return self.title
