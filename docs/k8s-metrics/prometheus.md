# Prometheus 
## Installation using Helm
```shell
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install my-prometheus prometheus-community/prometheus --version 25.0.0
```
access Prometheus Server by executing this command `kubectl port-forward svc/my-prometheus-server 8000:80`

## How to monitor a K8s Cluster

To monitor the Kubernetes cluster itself. Three aspects of cluster monitoring to consider are:

1. `The Kubernetes hosts (nodes)`: Classic sysadmin metrics such as cpu, load, disk, memory, etc.
2. `Orchestration level metrics`: Deployment state, resource requests, scheduling and api server latency, etc.
3. `Internal kube-system components`: Detailed service metrics for the scheduler, controller manager, dns service, etc.

Kube-state-metrics is a simple service that listens to the K8S API server and generates metrics about the state of the objects
such  as deployments, nodes and pods. It is important to note that kube-state-metrics is just a metrics endpoint. Other
entities need to scrape it and provide long term storage (e.g. Prometheus server).

Metrics-server is a cluster wide aggregator of resource usage data. The metrics server will only present the last data points
and its not in charge of long term storage.
Thus:
+ Kube-state metrics are focused on orchestration metadata: deployment, pod, replica, status, etc.
+ Metrics-server is focused on implementing the resource metrics API: CPU, file descriptors, memory, request latencies, etc.

### Monitoring the K8S nodes with Prometheus
Install Prometheus Node Exporters

```shell
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install my-prometheus-node-exporter prometheus-community/prometheus-node-exporter --version 4.23.1
```