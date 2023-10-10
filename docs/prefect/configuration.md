# Prefect
Prefect Components
- Prefect Server
- Prefect Worker
- Deployments
- Jupyterhub for scripting

## Jupyter Notebook

```shell
cd config/k8s/jupyter
kubectl apply -f .
```
`kubectl port-forward svc/notebook 8888:8888`

Then login to jupyter notebook using token `aces` open the terminal from jupyter and execute the following

```shell
pip install prefect
pip install s3fs
if [ -d "$HOME/.local/bin" ] ; 
then     
    PATH="$HOME/.local/bin:$PATH"; 
fi

prefect config set PREFECT_API_URL="http://prefect-server:4200/api"
```

## Install Minio Operator
Firstly you need to install the minio plugin in kubectl, to do so follow this link https://min.io/docs/minio/kubernetes/upstream/reference/kubectl-minio-plugin.html
```shell
kubectl minio init
kubectl minio tenant create aces \
         --namespace minio-operator \
         --pool aces \
         --servers 1 \
         --storage-class hostpath \
         --volumes 1 \
         --capacity 1Gi \
         --expose-minio-service \
         --disable-tls
```
after the execution of these commands you need to keep the credentials prompted and perform port forward to console service

`kubectl port-forward svc/console 9000:9090 -n minio-operator` and create a bucket called prefect-data

## Prefect Server
```shell
cd config/k8s
helm install prefect-server prefect/prefect-server --set postgresql.auth.password="prefect" --set postgresql.auth.username="prefect"
```

after this port forward the prefect dashboard `kubectl port-forward svc/prefect-server 4200:4200` go to work pools and create one called `sample` and its type should be Kubernetes.

## Create Deployment blocks
go to `scripts/` open the python script called and put the minio credentials prompted during Minio operator deployment and then execute the script from the jupyter shell
`python block.py`

## Prefect Agent
```shell
helm install prefect-agent prefect/prefect-agent -f values.yaml
```

## How to deploy flows
`prefect deployment build flows/simple_prometheus.py:prometheus_simple -n 'prometheus_simple' -ib kubernetes-job/prod -sb 'remote-file-system/minio' --pool sample`
`prefect deployment apply prometheus_simple-deployment.yaml`