# Django REST Framework skeleton

Django and REST Framework skeleton project.

## Versions

App | Version
--- | ---
Python | 2.7.12
Django | 1.11.11
DRF | 3.7.7

## What is included

- Preconfigured demo endpoints
- PostgreSQL as a Django database
- Scalable Docker and Docker Compose configuration (HAProxy)

## Docker Compose containers

- db (Django PostgreSQL database)
- web (Django application)
- lb (HAProxy load balancer)

# Project structure

    django-rest-skeleton/
    |---src                                     # django project folder
    |   |---drs                                 # django root configuration
    |   |   |---settings.py
    |   |   |---urls.py
    |   |   |---wsgi.py
    |   |---files
    |   |   |---tempaltes                       # view templates
    |   |   |   |---index.html
    |   |   |---media                           # images, sized cache and placeholder
    |   |   |   |---.gitignore
    |   |   |   |---placeholder.png
    |   |   |   |---README.md
    |   |   |---static
    |   |   |   |---placeholder.png
    |   |   |---README.md
    |   |---manage.py
    |---.gitignore
    |---.dockerignore
    |---Vagrantfile
    |---Dockerfile
    |---docker-compose.yml
    |---requirements.txt
    |---README.md

# Setup & Run

## Copy git repository

    git clone https://github.com/KenanBek/django-rest-skeleton.git
    cd django-rest-skeleton

## Run inside docker

    docker-compose build
    docker-compose up

## Run from local machine

    pip install -r requirements.txt
    cd src
    python manage.py runserver
