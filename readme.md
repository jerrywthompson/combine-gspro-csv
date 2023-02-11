sudo chmod 666 /var/run/docker.sock

docker build --tag docker-python-app .

docker run --name docker-python-app -it --rm --net=host docker-python-app

not working command yet
docker run --name docker-python-app -p 5001:5001 docker-python-app









old examples

# sudo chmod 666 /var/run/docker.sock
# docker login --username jt75611
# cd /home/jerry/develop/createRecipeWebpage

# push to dockerhub



# docker build --tag createrecipewebpage .
# If you want to test locally
       # docker run --name createrecipewebpage -p 5001:5001 createrecipewebpage
# docker tag createrecipewebpage:latest jt75611/createrecipewebpage:latest
# docker push  jt75611/createrecipewebpage:latest








sudo chmod 666 /var/run/docker.sock

docker build --tag flask-docker-demo-app .

docker run --name flask-docker-demo-app -p 5001:5001 flask-docker-demo-app

docker images

docker tag 5a821b66288b jt75611/flask_demo:latest


docker login --username jt75611

docker push jt75611/flask_demo


