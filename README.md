# Django Reservation System

This project is a Django-based reservation system that utilizes the Django REST framework with Ninja, Pydantic for data validation, PostgreSQL as the database, and Docker along with Docker Compose for deployment. The project also uses Poetry as the package manager and pytest for testing the application.

## Application Models

The reservation application includes the following models:

- Owner
- Listing
- Room
- Reservation

## Deployment Instructions

To deploy the project, follow these steps:

1. Copy the `.env.example` file and rename it to `.env`. Fill in the necessary configuration values in the `.env` file before deploying.

2. Build and start the Docker containers using the following command:
docker-compose up -d --build

3. To view the logs of the running containers, use the following command:
docker-compose logs -f --tail 500
## Additional Setup Steps

Before running the project, it's recommended to set up a `start.sh` file with the necessary commands. However, if not already set, you can execute the following command inside the Docker Compose environment (`docker-compose exec backend2 bash`) to migrate the database:
python3 manage.py migrate

## Project Creation Steps

The project was created by following these steps:

1. Initialize a Poetry project:

poetry init

2. Start a Django project using Poetry:
poetry run django-admin startproject config .

3. Create a Django app for the reservation system:
poetry run python3 manage.py startapp reservation_system



