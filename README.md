# ShopingList

Shopping List Application Deployment on Kubernetes

This README will guide you through deploying a Shopping List Application, consisting of a Flask backend and a React frontend, on Kubernetes. Both services will be deployed and will communicate internally using Kubernetes networking.

Prerequisites

Docker Desktop with Kubernetes enabled, or Minikube

kubectl CLI tool

Basic understanding of Docker and Kubernetes

Application Overview

Backend: Flask REST API to manage the shopping list.

Frontend: React-based UI for interacting with the shopping list.

Key Components

Dockerized Flask Backend: Handles requests for creating, reading, updating, and deleting shopping list items. The backend uses SQLite for data storage, which is embedded in the Python files. This is a conceptual implementation for simplicity; in a production environment, a separate StatefulSet or a Docker Compose setup with a volume-mounted database container would be recommended.

Dockerized React Frontend: Provides a user interface to interact with the shopping list.

Kubernetes Deployment: Manages the deployment and networking of both backend and frontend in the cluster.

Project Structure

flask-backend: Contains Flask API (app.py, requirements.txt, etc.)

react-frontend: Contains React application (src, public, etc.)

Kubernetes YAML Files: Files for deploying both applications and Ingress (flask-deployment.yaml, react-deployment.yaml, ingress.yaml)

Deployment Steps

1. Build Docker Images

First, build the Docker images for both backend and frontend.

Navigate to each directory (flask-backend and react-frontend) and run the following commands:

# Build Flask backend image
docker build -t flask-backend:latest .

# Build React frontend image
docker build -t react-frontend:latest .

If you are using Docker Desktop or Minikube, these images can be used directly in the Kubernetes cluster.

2. Deploy to Kubernetes

Make sure Kubernetes is enabled on Docker Desktop or Minikube is running.

A. Deploy the Flask Backend

Apply the deployment and service for Flask backend:

kubectl apply -f flask-deployment.yaml

Verify that the pods are running:

kubectl get pods

Verify that the service is running:

kubectl get svc

B. Deploy the React Frontend

Apply the deployment and service for React frontend:

kubectl apply -f react-deployment.yaml

Verify that the pods are running:

kubectl get pods

Verify that the service is running:

kubectl get svc

3. Set Up Ingress (Optional, Recommended for Better Routing)

To allow easy access to both frontend and backend through a single hostname, configure an Ingress.

Apply the Ingress configuration:

kubectl apply -f ingress.yaml

Update your local hosts file to route the custom hostname to your local Kubernetes cluster:

# Edit /etc/hosts (Linux/MacOS) or C:\Windows\System32\drivers\etc\hosts (Windows)
127.0.0.1 shopping-app.local

Access the application:

Frontend: http://shopping-app.local

Backend: http://shopping-app.local/shopping-list

4. Configuration in React App

In the React frontend (ShoppingList.jsx), ensure that you are using the service name defined in Kubernetes to communicate with the backend. Update URLs to use the Kubernetes DNS name for the backend:

const fetchItems = async () => {
    try {
        const response = await axios.get('http://flask-backend-service:5000/shopping-list');
        setItems(response.data);
    } catch (error) {
        console.error('Error fetching shopping list', error);
    }
};

Troubleshooting

Connection Refused: Ensure both services are running (kubectl get pods) and that the correct service names are used in the frontend.

CORS Issues: Make sure CORS is configured in the Flask backend to allow requests from the frontend.

Ingress Not Working: Verify that the Ingress controller is installed (minikube addons enable ingress for Minikube).

Cleaning Up

To delete the deployments and services from your Kubernetes cluster, run:

kubectl delete -f flask-deployment.yaml
kubectl delete -f react-deployment.yaml
kubectl delete -f ingress.yaml

Conclusion

By following this guide, you should be able to successfully deploy the Shopping List Application on Kubernetes, with proper internal communication between the backend and frontend using Kubernetes services and Ingress for routing.

This deployment serves as an example of deploying a simple application on Kubernetes and Docker Compose. The use of SQLite here is meant for demonstration purposes; for production, a dedicated StatefulSet or a containerized database with persistent volumes is recommended.
