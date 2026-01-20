brew update
# brew install hyperkit     # Warning: hyperkit has been deprecated because it is not maintained upstream!. It was disabled on 2025-06-21.

####################################
# Colima internally replaces:
# hyperkit
# docker-machine
####################################
brew install colima
colima start

####################################
# Install minikube
####################################
brew install minikube
minikube start --driver=docker


####################################
# Install kubectl-cli
####################################


####################################
# Create basic nginx deployment
####################################
kubectl create deployment nginx-depl --image=nginx
kubectl get replicaset