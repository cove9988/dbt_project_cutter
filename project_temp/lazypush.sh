#!/bin/bash

argument=${1:-"default commit"}
echo "commit comment:" $argument
git add .
git commit -m "$argument"
git pull
git push
