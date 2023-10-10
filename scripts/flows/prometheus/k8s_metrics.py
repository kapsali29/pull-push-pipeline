from .client import PrometheusClient


class K8SMetrics(PrometheusClient):
    def __init__(self, prometheus_base_url, metrics_str_tuple):
        super().__init__(prometheus_base_url)
        self.metrics_str_tuple = metrics_str_tuple

    def fetch_relevant_metrics(
            self
    ):
        response = self.get_metrics()
        if response.status_code == 200:
            response_json = response.json()
            all_metrics = response_json['data']
            relevant_metrics = list(filter(
                lambda metric: metric.startswith(self.metrics_str_tuple) is True,
                all_metrics
            ))
            return relevant_metrics
        else:
            return None