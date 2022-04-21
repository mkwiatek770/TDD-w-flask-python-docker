# TDD-w-flask-python-docker
course from testdriven.io


## Preface

[ ] docker
- how to get started with docker: https://youtu.be/iqqDU2crIEQ
- containers from scratch: https://youtu.be/8fi7uSYlOdc
- komenda chroot
- volumes
	named volumes:
	- docker volume create todo-db
	- docker run -dp 3000:3000 -v todo-db:/etc/todos getting-started
	bind mounts:
	- docker run -dp 3000:3000 -w /app -v "$(pwd):/app" node:12-alpine sh -c "yarn install && yarn run dev"
- networking (connecting many containers)
	- docker run -d --network todo-app --network-alias mysql --platform linux/amd64 -v todo-mysql-data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=secret -e MYSQL_DATABASE=todos mysql:5.7
- why using ENV variables shouldn't be used for secret data: https://diogomonica.com/2017/03/27/why-you-shouldnt-use-env-variables-for-secret-data/
- docker-compose
- docker scan (SNYK)
- best practices for python devs: https://testdriven.io/blog/docker-best-practices/
- ADD vs. COPY
- ENTRYPOINT vs. CMD
- .dockerignore


flask
- django vs. flask https://testdriven.io/blog/django-vs-flask/ & https://devel.tech/features/django-vs-flask & https://kite.com/blog/python/flask-vs-django-python
- authentication: who are you?
- authorization: what are you allowed to do?
