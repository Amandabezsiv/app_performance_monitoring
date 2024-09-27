from djongo import models

class PerformanceMetrics(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    response_time = models.FloatField()  # Time to response in seconds
    latency = models.FloatField()        # Latência em milissegundos
    cpu_usage = models.FloatField()      # Uso de CPU em porcentagem
    memory_usage = models.FloatField()   # Uso de memória em megabytes
    active_sessions = models.IntegerField()  # Número de sessões ativas
    page_load_time = models.FloatField()     # Tempo de carregamento da página em segundos

    class Meta:
        verbose_name = 'Performance Metric'
        verbose_name_plural = 'Performance Metrics'
