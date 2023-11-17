FROM node:16-alpine
 
WORKDIR /src
 
COPY package.json ./
RUN npm install

COPY . .
 
CMD [ "npm", "run", "dev"]
