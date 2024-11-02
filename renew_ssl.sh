#!/bin/bash
# Добавить в кронтаб root пользователя задачу на обновление SSL сертификата (запуск от root пользователя)
# 0 0 20 */2 * /home/finaflow/finaflow/renew_ssl.sh >> /var/log/renew_ssl.log 2>&1
export $(grep -v '^#' /home/finaflow/finaflow/.env | xargs)
service_nginx="prod_web"

check_docker_service() {
    docker service ls --format "{{.Name}}" | grep -q "$1"
}

login_registry() {
    echo "[$(date +"%Y-%m-%d %H:%M:%S")] Login to Registry..."
    echo $GITHUB | docker login ghcr.io -u yarvod --password-stdin
    if [ $? -eq 0 ]
    then
      echo "[$(date +"%Y-%m-%d %H:%M:%S")] Successfully login github"
    else
      echo "[$(date +"%Y-%m-%d %H:%M:%S")] Unable login github"
      exit 1
    fi
}

restart_services() {
    echo "[$(date +"%Y-%m-%d %H:%M:%S")] Restarting services..."
    env $(cat /home/finaflow/finaflow/.env | grep ^[A-Z] | xargs) docker stack deploy -c /home/finaflow/finaflow/docker-compose.prod.yaml --prune --with-registry-auth prod
    if check_docker_service $service_nginx;
    then
        echo "[$(date +"%Y-%m-%d %H:%M:%S")] Successfully restarted"
    else
        echo "[$(date +"%Y-%m-%d %H:%M:%S")] Unable restart"
        exit 1
    fi
}

update_certs() {
    echo "[$(date +"%Y-%m-%d %H:%M:%S")] Running Certbot..."
    certbot renew
    if [ $? -eq 0 ];
    then
      echo "[$(date +"%Y-%m-%d %H:%M:%S")] Successfully cert renewed"
    else
      echo "[$(date +"%Y-%m-%d %H:%M:%S")] Unable renew cert"
    fi
}

remove_service() {
    if check_docker_service "$1"; then
        echo "[$(date +"%Y-%m-%d %H:%M:%S")] Service Docker '$1' found, deleting..."
        docker service rm "$1"
        if ! check_docker_service "$1"; then
            echo "[$(date +"%Y-%m-%d %H:%M:%S")] Successfully removed $1"
        else
            echo "[$(date +"%Y-%m-%d %H:%M:%S")] Unable remove $1"
        fi
    else
        echo "[$(date +"%Y-%m-%d %H:%M:%S")] Service Docker '$1' not found, process certs..."
    fi
}

remove_service $service_nginx
sleep 10s
update_certs
login_registry
restart_services

echo "[$(date +"%Y-%m-%d %H:%M:%S")] Done!"
exit 0