from time import sleep

from prefect import flow, get_run_logger, task
from prometheus.k8s_metrics import K8SMetrics

@task
def init_client():
    k8s_client = K8SMetrics(
        prometheus_base_url="prometheus-server:80",
        metrics_str_tuple=("node_l")
    )
    return k8s_client

@task
def fetch_k8s_metrics(k8s_client):
    metrics_list = k8s_client.fetch_relevant_metrics()
    return metrics_list

@task
def get_metric_value(k8s_client, metric):
    response = k8s_client.intent_query(metric)
    response_data = response.json()
    logger = get_run_logger()
    logger.info(response_data)

@flow
def fetch_metrics_subset():
    k8s_client = init_client()
    metrics_list = fetch_k8s_metrics(k8s_client)
    
    for metric in metrics_list:
        get_metric_value(k8s_client, metric)
        