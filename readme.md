# My Resume as an API
A quick study of API framework using Django REST Framework and PostgreSQL

## What are the tools used for the project
* PostgreSQL
* Django Rest Framework
* Docker (for development and deployment to server)
* jenkins (to retrieve repository on github, copy relevant files to project folder and restart docker-compose in production)
* Nginx Proxy Manager

## References used
* Django REST Framework documentation
* Django documentation
* testdriven.io's Dockerizing Django with Postgres, Gunicorn and Nginx (partially for Django and Gunicorn)

## Lessons learned
* Django-REST Framework basic use (no authentication since it's all gets)
* Attaching a "legacy database" to django
* Adding restart policies to containers
* configuring jenkins hooks and pipelines