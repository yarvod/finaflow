FROM redis
COPY redis.conf /usr/local/etc/redis.conf
RUN apt-get update && apt-get install -y procps
CMD ["sh", "-c", "exec redis-server --requirepass \"$REDIS_PASSWORD\""]