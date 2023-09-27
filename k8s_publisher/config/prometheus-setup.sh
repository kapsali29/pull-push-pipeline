helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install my-prometheus-node-exporter prometheus-community/prometheus-node-exporter --version 4.23.1