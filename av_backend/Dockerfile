FROM python:3.11.0-slim-bullseye

ENV USER=root
#ENV USER=av
#RUN useradd ${USER}

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
    gettext \
 && rm -rf /var/lib/apt/lists/*

RUN pip install "gunicorn==20.1.0"

COPY requirements.txt /
RUN pip install -r /requirements.txt

# Use /app folder as a directory where the source code is stored.
WORKDIR /app

RUN mkdir "media"
RUN chown ${USER}:${USER} /app

COPY --chown=${USER}:${USER} . .

# User to run the build commands below and the server itself.
USER ${USER}

ENV DJANGO_SETTINGS_MODULE="av_backend.settings.production"
RUN python manage.py collectstatic --noinput --clear
RUN python manage.py compilemessages

ENTRYPOINT "./entrypoint.sh"
