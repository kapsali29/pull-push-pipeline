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
  Username: JEIZT100R234NO8Q9CF0
  Password: vVW4E8agAQ8twncmrKJaYELn2VBJZoUKqqwSmBF5
#