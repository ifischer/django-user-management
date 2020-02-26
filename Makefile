DOCKER_NAME = user-management
DOCKER_VOLUMES = -v $(PWD):/app
DOCKER_PORTS = -p 8000:8000
DOCKER_WO_PORTS = docker run $(ENV_FILES) $(DOCKER_VOLUMES) -it --rm $(DOCKER_NAME)
DOCKER_W_PORTS  = docker run $(ENV_FILES) $(DOCKER_VOLUMES) -it --rm $(DOCKER_PORTS) $(DOCKER_NAME)

build:
	docker build -t $(DOCKER_NAME) .

shell:
	$(DOCKER_WO_PORTS) bash

test:
	$(DOCKER_WO_PORTS) pytest

migrate:
	$(DOCKER_WO_PORTS) bash -c "python manage.py makemigrations \
		&& python manage.py migrate"

create_adminuser:
	$(DOCKER_W_PORTS) python manage.py create_adminuser

collectstatic:
	$(DOCKER_W_PORTS) python manage.py collectstatic --noinput

runserver:
	$(DOCKER_W_PORTS) python manage.py runserver 0.0.0.0:8000

django-shell:
	$(DOCKER_WO_PORTS) python manage.py shell_plus

django-urls:
	$(DOCKER_WO_PORTS) python manage.py show_urls
