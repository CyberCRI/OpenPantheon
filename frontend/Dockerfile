# Stage 0, "build-stage" to build and compile the frontend
FROM node:14-bullseye-slim as build-stage

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

COPY ./frontend/nginx.conf /etc/nginx/conf.d/default.conf

COPY --from=build-stage /app/dist/ /usr/share/nginx/html
