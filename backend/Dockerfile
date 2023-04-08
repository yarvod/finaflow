# pull official base image
FROM python:3.9.6
# set work directory
WORKDIR /app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ="Europe/Moscow"
# install dependencies
RUN apt-get update
RUN apt-get install postgresql postgresql-contrib -y
RUN pip install --upgrade pip
COPY requirements.txt .
COPY entrypoint.sh .
COPY wait-for-postgres.sh .
RUN chmod +x /app/wait-for-postgres.sh
RUN chmod +x /app/entrypoint.sh
RUN pip install -r requirements.txt
# run entrypoint.sh
ENTRYPOINT ["sh", "/app/entrypoint.sh"]