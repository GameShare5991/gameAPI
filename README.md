Code for the GameAPI

gameJSON file is a template to be used when making Create and Update operations. 

# build image: 
docker build . -t game-api

run image though docker: 
docker run --publish 5000:5000 game-api

# push image:
docker tag game-api jackjackzhou/game-api
docker push jackjackzhou/game-api

# kubectl create&run
minikube start
kubectl create -f game-app-deployment.yaml
minikube tunnel
minikube dashboard

# secret
kubectl create secret generic game-app-key\
--from-file=serviceAccountKey.json

kubectl describe secrets/game-app-key

# clean up
kubectl delete -f game-app-deployment.yaml