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

#
  Username: Y6E6WSSBZD7OXZ00ZSVU
  Password: GDefu2AKFtw7ZfFGUCFyOHJsBSrJ66XYOGRXMR0U
#