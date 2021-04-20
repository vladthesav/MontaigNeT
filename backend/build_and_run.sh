
#make sure port 3500 is clear
fuser -k 3500/tcp

#stop everything and remove all containers
docker kill $(docker ps -q)
docker rm $(docker ps -a -q)

#build docker container
docker build --tag mnet .

#run container
docker run -it --name mnet -p 3500:3500 mnet