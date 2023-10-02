# Prefect
Prefect Components
- Prefect Server
- Prefect Worker
- Deployments

## Installation
```shell
helm install prefect-server prefect/prefect-server --set postgresql.auth.password="prefect" --set postgresql.auth.username="prefect"
helm install prefect-worker prefect/prefect-worker -f values.yaml
```
Then it is needed to configure the prefect profile in order to build the deployments



## Apply deployment

```shell
`prefect config set PREFECT_API_URL="http://localhost:4200/api"`
`prefect deployment build flows/simple_flow.py:child -n 'child' -ib kubernetes-job/prod -sb 'remote-file-system/minio' --pool sample`
`prefect deployment apply child-deployment.yaml`
```