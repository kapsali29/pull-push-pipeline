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
  Username: ZUWQBKP0XJ5AA3310298
  Password: nYMDobmET2LNveuRMxBerbZJIywQllBuKUTHhXLu
#