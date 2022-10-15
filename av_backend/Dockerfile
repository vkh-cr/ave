FROM python:3.10.7-slim-bullseye

ENV USER=av

RUN useradd ${USER}

ENV PYTHONUNBUFFERED=1 \
    PORT=8000

EXPOSE ${PORT}

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
 && rm -rf /var/lib/apt/lists/*

RUN pip install "gunicorn==20.1.0"

COPY requirements.txt /
RUN pip install -r /requirements.txt

# Use /app folder as a directory where the source code is stored.
WORKDIR /app

RUN chown ${USER}:${USER} /app

COPY --chown=${USER}:${USER} . .

# User to run the build commands below and the server itself.
USER ${USER}

# TODO: Variables are not necessary in build time
ENV GOOGLE_APIS_CREDENTIALS_FILE=/dev/null
ENV AV_TEAM_SHEET_ID=None
RUN python manage.py collectstatic --noinput --clear

# TODO: entrypoint + proper gunicorn setup
CMD set -xe; python manage.py migrate --noinput; gunicorn av_backend.wsgi:application
