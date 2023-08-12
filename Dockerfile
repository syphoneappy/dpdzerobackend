FROM python:3.8-alpine3.16


RUN apk add --no-cache libpq-dev gcc musl-dev

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE dpdzero_project.settings

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
