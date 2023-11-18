# Dibimbing, Data Engineering Bootcamp

1. Clone This Repo.
2. Run `make docker-build` for x86 user, or `make docker-build-arm` for arm chip user.
<<<<<<< HEAD
3. Script to run DAG is /dags/dag_postgres.py and connect with /spark-scripts/try.py
=======
3. Dag file in /dags/dag_postgres.py and connect with /spark-scripts.try.py/
>>>>>>> 03b3e9a0643565b75d1f23fd9b79138f18e6dbbf
---
```
## docker-build			- Build Docker Images (amd64) including its inter-container network.
## docker-build-arm		- Build Docker Images (arm64) including its inter-container network.
## postgres			- Run a Postgres container
## spark			- Run a Spark cluster, rebuild the postgres container, then create the destination tables
## jupyter			- Spinup jupyter notebook for testing and validation purposes.
## airflow			- Spinup airflow scheduler and webserver.
## metabase			- Running Metabase app.
## clean			- Cleanup all running containers related to the challenge.
```


---
