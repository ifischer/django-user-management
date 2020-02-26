FROM python:3.7.6-slim

WORKDIR /app

COPY requirements.txt ./
COPY requirements-test.txt ./
COPY requirements-dev.txt ./

RUN pip install -r requirements.txt
RUN pip install -r requirements-test.txt
RUN pip install -r requirements-dev.txt

COPY . .

RUN pip install .

EXPOSE 8000

CMD python manage.py collectstatic --noinput && \
    python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py runserver 0.0.0.0:8000
