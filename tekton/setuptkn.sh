#!/bin/bash

echo "***Set user to have cluster admin permissions***"
export USER=$(kubectl config current-context)
kubectl create clusterrolebinding bx-role-binding --clusterrole=cluster-admin --user=$USER

echo "***Install tekton pipeline controller***"
kubectl apply --filename https://storage.googleapis.com/tekton-releases/pipeline/latest/release.yaml

echo "***Installing git-clone task***"
kubectl apply -f https://raw.githubusercontent.com/tektoncd/catalog/main/task/git-clone/0.9/git-clone.yaml