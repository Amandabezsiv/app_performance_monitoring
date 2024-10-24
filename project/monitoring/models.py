from djongo import models

class PerformanceMetrics(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    response_time = models.FloatField()  
    latency = models.FloatField()        
    cpu_usage = models.FloatField()      
    memory_usage = models.FloatField()   
    active_sessions = models.IntegerField()  
    page_load_time = models.FloatField()    

    class Meta:
        verbose_name = 'Performance Metric'
        verbose_name_plural = 'Performance Metrics'

# AccessLog model was created to record the last accesses of the application
class AccessLog(models.Model):
    accessed_at = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=255)
    user_agent = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.accessed_at} - {self.url}"
