from django.shortcuts import render
from .models import Report
from monitoring.models import PerformanceMetrics, AccessLog
import matplotlib.pyplot as plt
import io, os

# I am only creating the cpu usage graph as an example but a graph can be
# created for the other metrics used

def generate_graphs(metrics):
    # Create CPU usage graph
    cpu_usage = [metric.cpu_usage for metric in metrics]
    plt.figure(figsize=(10, 5))
    plt.plot(cpu_usage, label='CPU Usage')
    plt.title('CPU usage over time')
    plt.xlabel('Time')
    plt.ylabel('CPU Usage (%)')
    plt.legend()
    # Save graph to buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return buf

# I also created a graph of last accesses to know the main URLs accessed
def generate_access_graph():
    last_accesses = AccessLog.objects.order_by('-accessed_at')[:10]
    access_times = [access.accessed_at for access in last_accesses]
    access_urls = [access.url for access in last_accesses]

    plt.figure(figsize=(12, 6))  
    plt.barh(access_urls, range(len(access_urls)), color='skyblue')  
    plt.title('Last Access', fontsize=16)  
    plt.xlabel('Number of Access', fontsize=14)  
    plt.ylabel('URLs', fontsize=14)  
    plt.xticks(rotation=45, fontsize=12)  
    plt.yticks(fontsize=12)  
    plt.tight_layout()  
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return buf


def generate_report(request):
    metrics = PerformanceMetrics.objects.all()

    # Reports_dir is the variable that will store the path where the reports will be saved
    reports_dir = os.path.join('media', 'reports')  
    
    # Create report
    report = Report.objects.create(title='Performance Report', content='See the attached graphics.')

    cpu_usage_graph = generate_graphs(metrics)
    access_graph = generate_access_graph()

    # Saved graph
    cpu_usage_file_path = os.path.join(reports_dir, 'cpu_usage.png')
    with open(cpu_usage_file_path, 'wb') as f:
        f.write(cpu_usage_graph.read())

    access_file_path = os.path.join(reports_dir, 'access_graph.png')
    with open(access_file_path, 'wb') as f:
        f.write(access_graph.read())

    return render(request, 'reports/report_detail.html', {
        'report': report,
        'cpu_usage_graph_url': f"{request.build_absolute_uri('/media/reports/cpu_usage.png')}",
        'access_graph_url': f"{request.build_absolute_uri('/media/reports/access_graph.png')}",
    })