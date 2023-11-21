FROM node:16-alpine AS compile-image
LABEL maintainer="Sylvain BOILY <sylvain@wazo.io>"

WORKDIR /src
 
COPY package.json ./
RUN npm install

COPY . .

RUN npm run build
COPY manifest-portal.json ./dist

FROM caddy as build-image
COPY --from=compile-image /src/dist /usr/share/caddy/

COPY Caddyfile /etc/caddy
