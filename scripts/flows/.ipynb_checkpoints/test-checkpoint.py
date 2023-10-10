import requests
from prometheus.k8s_metrics import K8SMetrics

client = K8SMetrics(
    prometheus_base_url="prometheus-server:80",
    metrics_str_tuple=("node_l")
)

data = client.fetch_relevant_metrics()
print(data)