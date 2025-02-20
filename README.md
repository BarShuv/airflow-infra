# 🏗️ Airflow Infra

This repository contains the infrastructure setup for running **Apache Airflow** in a Docker-based environment.

## 🚀 Getting Started

### 1️⃣ Configure Environment Variables  
Before starting the Airflow instance, update the **`.env`** file with the necessary configurations.

### 2️⃣ Start Airflow  
Run the following command to start the Airflow services:

```sh
make start
```
This command will:

Set up the necessary directories
Initialize the Airflow database
Create an admin user (if not already created)
Start the Airflow webserver, scheduler, and Ngrok tunnel

### 3️⃣ Access Airflow
Once the setup is complete, you can access the Airflow UI at:
📌 http://localhost:8080

If using Ngrok, find the public URL by running:

```sh
docker logs airflow_ngrok --tail 10
```

🛑 Stopping Airflow
To shut down all running containers:

```sh
make stop
```

🔄 Restart Airflow
To restart all services:

```sh
make restart
```

🛠️ Troubleshooting
Logs are available under the logs/ directory inside the project.
To inspect logs for a specific DAG execution, run:

```sh
docker exec -it airflow_webserver cat /opt/airflow/logs/dag_id=<DAG_ID>/run_id=<RUN_ID>/task_id=<TASK_ID>/attempt=1.log
```
📌 Notes
Ensure Make, Docker and Docker Compose are installed before running the setup.
🎯 Now you are ready to run and manage workflows with Airflow! 🚀



