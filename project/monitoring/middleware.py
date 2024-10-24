import time, psutil
from monitoring.models import PerformanceMetrics, AccessLog
from alerts.models import Alert 
from django.contrib.sessions.models import Session

# Define thresholds for the metrics
CPU_LIMIT = 70  # Percent
MEMORY_LIMIT = 75  # Percent
RESPONSE_TIME_LIMIT = 2  # In seconds
LATENCY_LIMIT = 300  # In milliseconds
ACTIVE_SESSIONS_LIMIT = 100  

class PerformanceMonitoringMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        # Process the request
        response = self.get_response(request)

        # Calculate response time and latency
        response_time = time.time() - start_time
        latency = response_time * 1000  # In milliseconds

        # Collect CPU and memory usage using psutil
        cpu_usage = psutil.cpu_percent(interval=None)
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.used / (1024 * 1024)  # Convert to megabytes

        # Get the number of active sessions
        active_sessions = Session.objects.count()

        # Calculate page load time (simulated)
        page_load_time = response_time  # Here, response time can be used as a proxy

        # Save the metrics to MongoDB
        PerformanceMetrics.objects.create(
            response_time=response_time,
            latency=latency,
            cpu_usage=cpu_usage,
            memory_usage=memory_usage,
            active_sessions=active_sessions,
            page_load_time=page_load_time
        )

        # Check if metrics exceed thresholds and create alerts
        if cpu_usage > CPU_LIMIT:
            Alert.objects.create(alert_type='CPU', severity='high', message='High CPU usage!')

        if memory_usage > MEMORY_LIMIT:
            Alert.objects.create(alert_type='Memory', severity='high', message='High Memory usage!')

        if response_time > RESPONSE_TIME_LIMIT:
            Alert.objects.create(alert_type='Response Time', severity='high', message='High response time!')

        if latency > LATENCY_LIMIT:
            Alert.objects.create(alert_type='Latency', severity='high', message='High latency!')

        if active_sessions > ACTIVE_SESSIONS_LIMIT:
            Alert.objects.create(alert_type='Active Sessions', severity='high', message='Too many active users!')

        AccessLog.objects.create(url=request.path, user_agent=request.META.get('HTTP_USER_AGENT'))  
        return response
