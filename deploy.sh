#!/usr/bin/env bash

IMAGE_NAME="docker.sepior.net:5000/sepior/docker-filebeat"
source ./local/creds.sh
docker login -u $DOCKER_USER -p $DOCKER_PASSWORD "https://docker.sepior.net:5000"

docker build --tag $IMAGE_NAME --no-cache 5-stdin 

docker push $IMAGE_NAME
