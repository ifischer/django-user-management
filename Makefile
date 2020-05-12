DOCKER_NAME = user-management
DOCKER_VOLUMES = -v $(PWD):/app
DOCKER_PORTS = -p 8000:8000
DOCKER_WO_PORTS = docker run $(ENV_FILES) $(DOCKER_VOLUMES) -e DJANGO_SETTINGS_MODULE=user_management_site.settings -it --rm $(DOCKER_NAME)
DOCKER_W_PORTS  = docker run $(ENV_FILES) $(DOCKER_VOLUMES) -it --rm $(DOCKER_PORTS) $(DOCKER_NAME)

VIRTUALENV_NAME = .venv

build:
	docker build -t $(DOCKER_NAME) .

shell:
	$(DOCKER_WO_PORTS) bash

test:
	$(DOCKER_WO_PORTS) pytest

migrate:
	$(DOCKER_WO_PORTS) bash -c "python manage.py makemigrations \
		&& python manage.py migrate"

django-create-adminuser:
	$(DOCKER_WO_PORTS) python manage.py create_adminuser

collectstatic:
	$(DOCKER_WO_PORTS) python manage.py collectstatic --noinput

django-runserver:
	$(DOCKER_W_PORTS) python manage.py runserver 0.0.0.0:8000

django-shell:
	$(DOCKER_WO_PORTS) python manage.py shell_plus

django-urls:
	$(DOCKER_WO_PORTS) python manage.py show_urls

pytest-querycount:
	$(DOCKER_WO_PORTS) pytest --querycount 0

virtualenv:
	virtualenv --python=`which python3` $(VIRTUALENV_NAME)
	$(VIRTUALENV_NAME)/bin/pip install -r requirements.txt
	$(VIRTUALENV_NAME)/bin/pip install -r requirements-dev.txt
	$(VIRTUALENV_NAME)/bin/pip install -r requirements-test.txt
	$(VIRTUALENV_NAME)/bin/pip install -e .
	@echo "Activate virtualenv:\n. $(VIRTUALENV_NAME)/bin/activate