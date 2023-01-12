#!/bin/bash

echo "Set user to have cluster admin permissions"

echo "Install tekton pipeline controller"

echo "Installing git-clone task"
kubectl apply -f https://raw.githubusercontent.com/tektoncd/catalog/main/task/git-clone/0.9/git-clone.yaml