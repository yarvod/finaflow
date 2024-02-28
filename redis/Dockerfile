FROM redis:5.0
RUN apt-get update && apt-get install -y procps
CMD ["sh", "-c", "exec redis-server --requirepass \"$REDIS_PASSWORD\""]