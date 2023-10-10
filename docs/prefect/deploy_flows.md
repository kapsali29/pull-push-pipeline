# Prefect Cli


## Apply deployments
```shell
`prefect config set PREFECT_API_URL="http://prefect-server:4200/api"`
`prefect deployment build flows/simple_prometheus.py:prometheus_simple -n 'prometheus_simple' -ib kubernetes-job/prod -sb 'remote-file-system/minio' --pool sample`
`prefect deployment apply prometheus_simple-deployment.yaml`
```

```shell
`prefect config set PREFECT_API_URL="http://prefect-server:4200/api"`
`prefect deployment build flows/fetch_metrics_tiny_set.py:fetch_metrics_subset -n 'fetch_metrics_subset' -ib kubernetes-job/prod -sb 'remote-file-system/minio' --pool sample`
`prefect deployment apply fetch_metrics_subset-deployment.yaml`
```