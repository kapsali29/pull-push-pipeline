## Step 0 - Add bitnami charts to helm repos
create namespace `kafka`
```shell
helm repo add bitnami https://charts.bitnami.com/bitnami
```
## Step 1 - Install Zookeeper with 1 node

```shell
helm install zookeeper bitnami/zookeeper \
  --set replicaCount=1 \
  --set auth.enabled=false \
  --set allowAnonymousLogin=true -n kafka
```
## Step 2 - Deploy Apache Kafka - 1 node

```shell
helm install kafka bitnami/kafka \
  --set zookeeper.enabled=false \
  --set replicaCount=1 \
  --set externalZookeeper.servers=zookeeper \
  --set listeners.advertisedListeners="CLIENT://kafka.kafka.svc.local:9092" -n kafka
```
