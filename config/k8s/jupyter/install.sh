helm repo add jupyterhub https://jupyterhub.github.io/helm-chart/
helm show values jupyterhub/jupyterhub > values.yaml
helm upgrade --cleanup-on-fail --install my-jupyter jupyterhub/jupyterhub --values values.yaml