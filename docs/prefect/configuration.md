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

`prefect config set PREFECT_API_URL="http://localhost:4200/api"`

` prefect deploy -n child/default`

## Install MinIO (TODO)

```shell
    # example using s3 to store flow code
    push:
      - prefect_aws.deployments.steps.push_to_s3:
          bucket: minio-flows
          folder: param
          client_parameters:
            endpoint_url: http://localhost:9000
    pull:
      - prefect_aws.deployments.steps.pull_from_s3:
          bucket: minio-flows
          folder: param
          client_parameters:
            endpoint_url: http://minio:9000
```