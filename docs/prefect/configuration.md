# Prefect
Prefect Components
- Prefect Server
- Prefect Worker
- Deployments
- Jupyterhub for scripting

## Installation
```shell
helm install prefect-server prefect/prefect-server --set postgresql.auth.password="prefect" --set postgresql.auth.username="prefect"
helm install prefect-worker prefect/prefect-worker -f values.yaml
```
Then it is needed to configure the prefect profile in order to build the deployments

### Set Jupyter for scripting

```shell
/bin/bash
pip install prefect
pip install s3fs

if [ -d "$HOME/.local/bin" ] ; 
then     
    PATH="$HOME/.local/bin:$PATH"; 
fi
```


## Apply deployment
```shell
`prefect config set PREFECT_API_URL="http://prefect-server:4200/api"`
`prefect deployment build flows/simple_flow.py:child -n 'child' -ib kubernetes-job/prod -sb 'remote-file-system/minio' --pool sample`
`prefect deployment apply child-deployment.yaml`
```