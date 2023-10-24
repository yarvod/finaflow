FROM node:18-alpine as BUILD_STAGE
WORKDIR /app
COPY package.json .
COPY . .
RUN npm install
RUN apk update && apk add tzdata
ENV TZ=Europe/Moscow
RUN npm run build


FROM nginx:1.22.0-alpine
RUN apk add --no-cache esh openssl
COPY nginx-entrypoint.sh .
COPY default.conf.esh /etc/nginx/
COPY --from=BUILD_STAGE /app/dist /usr/share/nginx/html
ENV TZ="Europe/Moscow"
RUN chmod +x nginx-entrypoint.sh
ENTRYPOINT ["./nginx-entrypoint.sh"]