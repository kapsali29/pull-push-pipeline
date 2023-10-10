from time import sleep

from prefect import flow, get_run_logger, task
from prometheus.client import PrometheusClient


@task
def init_client():
    prometheus_client = PrometheusClient(
        prometheus_base_url="prometheus-server:80"
    )
    return prometheus_client

@task
def list_of_labels(prometheus_client):
    response = prometheus_client.get_all_labels()
    data = response.json()
    return data

@task
def print_labels(labels):
    logger = get_run_logger()
    logger.info(labels)


@flow
def prometheus_simple() -> None:
    prometheus_client = init_client()
    labels = list_of_labels(prometheus_client)
    print_labels(labels)


if __name__ == "__main__":
    prometheus_simple()
