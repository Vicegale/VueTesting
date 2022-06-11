FROM node:lts-alpine

#Install webserver
RUN npm install -g http-server

#set /app workdir
WORKDIR /app

#Copy package manifests (package.json and package-lock.json)
#This step is done first in order to be able to cache the dependencies in the image after running npm install
#This is done to avoid the need to run npm install every time the image is built
COPY package*.json ./

#Install packages
RUN npm install

#Copy project files
COPY . .

#Build the project
RUN npm run build

EXPOSE 8080

#Start application
CMD ["http-server", "dist"]