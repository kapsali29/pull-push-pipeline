from prometheus_client.k8s_metrics import K8SMetrics

metrics_str_tuple = ('node_', 'container_', 'kubelet_')
prometheus_base_url = 'localhost:8000'
k8s = K8SMetrics(prometheus_base_url, metrics_str_tuple)
results = k8s.fetch_relevant_metrics()
print(results)