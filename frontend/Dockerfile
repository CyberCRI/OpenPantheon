# Stage 0, "build-stage" to build and compile the frontend
FROM node:14-bullseye-slim as build-stage

# Required on non x86_64 to compile some of the dependencies
RUN apt-get update && \
    apt-get install -y python3 build-essential && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./frontend/package.json ./frontend/yarn.lock /app/

RUN yarn install --pure-lockfile --non-interactive

COPY ./frontend/ /app/

ARG BACKEND_URL=http://localhost:8000
ENV VUE_APP_BACKEND_URL=${BACKEND_URL}

# Comment out the next line to disable tests
RUN yarn test:unit

RUN yarn build


# Stage 1, based on Nginx, to have only the compiled app, ready for production with Nginx
FROM nginx:1.20

ARG BACKEND_URL=http://localhost:8000
ENV ADD_HEADER_HSTS="" \
    BACKEND_URL=${BACKEND_URL}

COPY ./frontend/nginx.conf.template /etc/nginx/templates/default.conf.template

EXPOSE 8080

COPY --from=build-stage /app/dist/ /usr/share/nginx/html
