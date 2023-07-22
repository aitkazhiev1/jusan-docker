#1/bin/bash
curl -O https://stepik.org/media/attachments/lesson/691221/nginx.conf
docker run -d -p 7777:80 --name jusan-docker-bind -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf nginx:mainline
echo "Контейнер создан"
