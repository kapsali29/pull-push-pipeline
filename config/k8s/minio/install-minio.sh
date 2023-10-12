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
  Username: ZAOPUBB550HDJBUJUUCN
  Password: RJOxNdQrXGhTtt7Gc4X3sC2j6YIWED8ELLJhSRsL
#