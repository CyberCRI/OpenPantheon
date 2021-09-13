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

RUN yarn start
