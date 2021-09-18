FROM python:3.9-alpine AS {{cookiecutter.project_slug}}

WORKDIR /app

ENV PYTHONFAULTHANDLER=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONHASHSEED=random
ENV PYTHONDONTWRITEBYTECODE 1
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100

# Env vars
ENV SECRET_KEY ${SECRET_KEY}
ENV TELEGRAM_TOKEN ${TELEGRAM_TOKEN}

# install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN mkdir requirements
ADD ./requirements/ /app/requirements
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements/prod.txt

# copy project
COPY . .

# start bot
EXPOSE 8000
CMD ["python3", "manage.py", "runbot"]
