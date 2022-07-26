Code for the GameAPI

gameJSON file is a template to be used when making Create and Update operations. 

build image: 
docker build . -t game-api

run image though docker: 
docker run --publish 5000:5000 game-api


kubectl create -f game-app-deployment.yml
kubectl run game-pod --image=game-api --port=6379