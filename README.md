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
## clean			- Cleanup all running containers related to the challenge.
```

### Count the number of churned customers in retail table
<img width="1379" alt="Jepretan Layar 2023-09-24 pukul 16 06 25" src="https://github.com/ayarzuki/spark-airflow-postgres/assets/48020037/91b2a9c6-3de1-4a45-baa4-ab29b646bd24">

### Rank each product based on the quantity sold in retail table
<img width="1321" alt="Jepretan Layar 2023-09-24 pukul 16 11 45" src="https://github.com/ayarzuki/spark-airflow-postgres/assets/48020037/9a110b13-eaa0-47f5-8ada-89f7865dc1a5">

---
