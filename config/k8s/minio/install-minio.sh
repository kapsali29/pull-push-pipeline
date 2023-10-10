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
  Username: YKZZDGSA064XEMUW8FAZ
  Password: 8bORSc9SvWLGiqW5KgyLAdXUx6EE4nrBy0n5N61A
#