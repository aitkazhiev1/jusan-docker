#1/bin/bash
docker run -d -p 8181:80 --name jusan-docker-exec nginx:mainline
docker exec -it jusan-docker-exec /bin/bash
cat << EOF > /etc/nginx/conf.d/jusan-docker-exec.conf
server {
    listen 80;
    server_name jusan.singularity;

    location / {return 200 'Hello, from jusan-docker-exec';}
    location /home {return 201 'This is my home!';}
    location /about {return 202 'I am just an exercise!';}
}
EOF
nginx -s reload
