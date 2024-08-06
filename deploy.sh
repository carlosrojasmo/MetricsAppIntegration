#!/bin/bash

IMAGE_NAME="metrics-app"
CONTAINER_NAME="metrics-app-container"


docker build -t $IMAGE_NAME .
# En caso de que ya exista un contenedor con el mismo nombre
if [ "$(docker ps -aq -f name=$CONTAINER_NAME)" ]; then
    docker rm -f $CONTAINER_NAME
fi

docker run -d -p 5000:5000 --name $CONTAINER_NAME --restart always $IMAGE_NAME
echo "Despliegue completado. La aplicación se está ejecutando en http://localhost:5000/metrics"
