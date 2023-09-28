helm install prefect-server prefect/prefect-server --set postgresql.auth.password="prefect" --set postgresql.auth.username="prefect"
helm install prefect-worker prefect/prefect-worker -f values.yaml
