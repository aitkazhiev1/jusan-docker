docker build -t jusan-fastapi-final:dockerized .
docker run -d -p 8080:8080 --name jusan-dockerize jusan-fastapi-final:dockerized

