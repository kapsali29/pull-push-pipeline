from time import sleep

from prefect import flow, get_run_logger, task
from prometheus.k8s_metrics import K8SMetrics
from kafka.client import KafkaObject


@task
def init_client():
    k8s_client = K8SMetrics(
        prometheus_base_url="prometheus-server:80",
        metrics_str_tuple=("node_l")
    )
    return k8s_client


@task
def init_kafka_object():
    kafka_obj = KafkaObject(
        bootstrap_servers="broker:29092"
    )
    return kafka_obj


@task
def fetch_k8s_metrics(k8s_client):
    metrics_list = k8s_client.fetch_relevant_metrics()
    return metrics_list


@task
def get_metric_value(k8s_client, metric):
    response = k8s_client.intent_query(metric)
    response_data = response.json()
    return response_data


@flow
def fetch_metrics_subset():
    k8s_client = init_client()
    kafka_obj = init_kafka_object()
    metrics_list = fetch_k8s_metrics(k8s_client)

    for metric in metrics_list:
        metric_data = get_metric_value(
            k8s_client=k8s_client,
            metric=metric
        )
        kafka_obj.producer(
            msg=metric_data,
            topic="tiny-example"
        )
