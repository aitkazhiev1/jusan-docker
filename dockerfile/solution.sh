#1/bin/bash
curl -O https://stepik.org/media/attachments/lesson/686238/jusan-dockerfile.conf
curl -O https://stepik.org/media/attachments/lesson/686238/jusan-dockerfile.zip
# Создал докерфайл:
# cat Dockerfile
# FROM nginx:mainline

# COPY jusan-dockerfile.conf /etc/nginx/conf.d/default.conf

# COPY jusan-dockerfile /var/www/jusan-dockerfile
docker build -t nginx:jusan-dockerfile .
docker run -d -p 6060:80 --name jusan-dockerfile nginx:jusan-dockerfile

