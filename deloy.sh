#!/bin/bash
cd ~/myapp
echo "Pull code..."
git pull origin main 
echo "Build Docker..."
docker build -t myapp .
echo "Stop old container..."
docker stop $(docker ps -q)
echo "Run new container..."
docker run -d -p 3000:80 myapp
echo "DONE DEPLOY"
