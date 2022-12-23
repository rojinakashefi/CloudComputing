# Get coin price using Docker & kubernetes

This project consists of 4 steps:

## First step:

    Build a alphine container consists of curl command.

   **Keywords** : Docker build, Docker tag, Docker image, Docker ps, Docker image push, Docker image pull, Docker file

## Second step:

    Write an api for requesting coin prices and save it in redis with expiration time and connect our application on container to our redis image.

  **Keywords**: Flask, Docker file, Redis, Docker exec, Docker volume, Docker network

## Third step:

Create Deployment.yaml, Servie.yaml and Config-map.yaml for setting pods and kubernetes configs.

Keywords: minikube, kubectl get all, kubectl apply.

## Fourth step:

Request to our application, which itself send a request to coin website and save the result on redis database, using curl of alphine image on first step via kubectl

Keywords: Kubectl run




