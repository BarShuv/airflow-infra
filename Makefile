# Load environment variables from .env
include .env
export $(shell sed 's/=.*//' .env)

.PHONY: setup init-db create-user start stop restart clean-logs

# Setup - Create necessary directories
setup:
	mkdir -p dags logs plugins

# Initialize Airflow database
init-db:
	docker-compose down
	docker-compose run --rm webserver airflow db init

# Create Airflow Admin User (using environment variables)
create-user:
	docker-compose run --rm webserver airflow users list | grep -q "$$AIRFLOW_USER" || \
	docker-compose run --rm webserver airflow users create \
	    --username $$AIRFLOW_USER \
	    --password $$AIRFLOW_PASSWORD \
	    --firstname Admin \
	    --lastname User \
	    --role $$AIRFLOW_ROLE \
	    --email $$AIRFLOW_EMAIL

# Start Airflow
start: setup init-db create-user
	docker-compose up -d

# Stop all Airflow services
stop:
	docker-compose down

# Restart Airflow
restart: stop start

# Cleanup logs
clean-logs:
	sudo rm -rf logs/*
