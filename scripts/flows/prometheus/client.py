import requests


class PrometheusClient(object):
    def __init__(
            self,
            prometheus_base_url,
            http_protocol='http'
    ):
        self.prometheus_base_url = prometheus_base_url
        self.http_protocol = http_protocol

    @staticmethod
    def http(
            url,
            method="GET",
            **kwargs
    ):
        response = requests.request(
            method=method,
            url=url,
            **kwargs
        )
        return response

    def get_all_labels(
            self
    ):
        response = self.http(
            url=f'{self.http_protocol}://{self.prometheus_base_url}/api/v1/labels'
        )
        return response

    def get_label_values(
            self,
            label
    ):
        response = self.http(
            url=f'{self.http_protocol}://{self.prometheus_base_url}/api/v1/label/{label}/values'
        )
        return response

    def get_metrics(
            self
    ):
        response = self.http(
            url=f'{self.http_protocol}://{self.prometheus_base_url}/api/v1/label/__name__/values'
        )
        return response

    def intent_query(
            self,
            metric,
            time=None
    ):
        query_url = f'{self.http_protocol}://{self.prometheus_base_url}/api/v1/query?query={metric}'
        if time:
            query_url = f'{query_url}&time={time}'
        response = self.http(
            url=query_url
        )
        return response

    def range_query(
            self,
            metric,
            start,
            end
    ):
        range_url = f'{self.http_protocol}://{self.prometheus_base_url}/api/v1/query_range?query={metric}'
        if start:
            range_url = f'{range_url}&start={start}'
        if end:
            range_url = f'{range_url}&end={end}'
        response = self.http(
            url=range_url
        )
        return response