from prometheus_client import start_http_server, Counter, Gauge, REGISTRY
import time
import os
import psutil  # To get system CPU and memory stats

# Flag to check if the metrics have been defined
metrics_defined = False

def define_metrics():
    global metrics_defined

    # Check if metrics are already defined
    if not metrics_defined:
        # Define Prometheus metrics globally
        global REQUESTS, CPU_USAGE, MEMORY_USAGE
        REQUESTS = Counter('http_requests_total', 'Total HTTP Requests', registry=REGISTRY)
        CPU_USAGE = Gauge('process_cpu_seconds_total', 'Total CPU Time Used by Process', registry=REGISTRY)
        MEMORY_USAGE = Gauge('process_resident_memory_bytes', 'Memory Usage of the Process', registry=REGISTRY)
        
        metrics_defined = True

def process_request():
    REQUESTS.inc()

def update_metrics():
    # Update CPU usage
    cpu_time = psutil.Process(os.getpid()).cpu_times().user
    CPU_USAGE.set(cpu_time)

    # Update Memory usage
    memory_usage = psutil.Process(os.getpid()).memory_info().rss  # in bytes
    MEMORY_USAGE.set(memory_usage)

if __name__ == '__main__':
    define_metrics()  # Ensure metrics are defined only once
    start_http_server(5001)
    while True:
        process_request()
        update_metrics()
        time.sleep(1)
