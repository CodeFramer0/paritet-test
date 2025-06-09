FROM node:20-alpine AS frontend_build
WORKDIR /app
COPY package*.json ./
RUN npm install
ARG VITE_API_TOKEN
ENV VITE_API_TOKEN=$VITE_API_TOKEN
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=frontend_build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
