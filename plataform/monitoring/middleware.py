import time
import psutil
from monitoring.models import PerformanceMetrics
from django.contrib.sessions.models import Session

class PerformanceMonitoringMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        # Processa a requisição
        response = self.get_response(request)

        # Calcular o tempo de resposta e latência
        response_time = time.time() - start_time
        latency = response_time * 1000  # Em milissegundos

        # Coletar uso de CPU e memória usando psutil
        cpu_usage = psutil.cpu_percent(interval=None)
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.used / (1024 * 1024)  # Converter para megabytes

        # Coletar o número de sessões ativas
        active_sessions = Session.objects.count()

        # Calcular o tempo de carregamento da página (simulado)
        page_load_time = response_time  # Aqui, o tempo de resposta pode ser usado como proxy

        # Salvar as métricas no MongoDB
        PerformanceMetrics.objects.create(
            response_time=response_time,
            latency=latency,
            cpu_usage=cpu_usage,
            memory_usage=memory_usage,
            active_sessions=active_sessions,
            page_load_time=page_load_time
        )

        return response
