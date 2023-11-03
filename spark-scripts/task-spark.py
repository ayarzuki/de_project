# from datetime import datetime, timedelta

# import pyspark
# import os
# import json
# import argparse

# # from dotenv import load_dotenv
# # from pathlib import Path
# from pyspark.sql.types import StructType
# from pyspark.sql.functions import to_timestamp,col,when

# from pyspark.sql import SparkSession

# # def main():
# # dotenv_path = Path('/resources/.env')
# # load_dotenv(dotenv_path=dotenv_path)

# # postgres_host = os.getenv('dataeng-postgres')
# # postgres_db = os.getenv('postgres_db')
# # postgres_user = os.getenv('user')
# # postgres_password = os.getenv('password')
# postgres_host = 'dataeng-postgres'
# postgres_db = 'postgres_db'
# postgres_user = 'user'
# postgres_password = 'password'

# sparkcontext = pyspark.SparkContext.getOrCreate(conf=(
#         pyspark
#         .SparkConf()
#         .setAppName('retail-analysis')
#         .setMaster('local')
#         .set("spark.jars", "/opt/bitnami/spark/jars/postgresql-42.2.18.jar")
#     ))
# sparkcontext.setLogLevel("WARN")

# spark = pyspark.sql.SparkSession(sparkcontext.getOrCreate())

# # print(spark)
# # print("hello world")

# jdbc_url = f'jdbc:postgresql://{postgres_host}/{postgres_db}'
# # jdbc_url = "jdbc:postgresql://postgres:5432/airflow"
# jdbc_properties = {
#         'user': postgres_user,
#         'password': postgres_password,
#         'driver': 'org.postgresql.Driver',
#         'stringtype': 'unspecified'
# }

#     # jdbc_properties = {
#     #     'user': postgres_user,
#     #     'password': postgres_password,
#     #     'driver': 'org.postgresql.Driver'
#     # }

#     # print(jdbc_url)
#     # print(jdbc_properties)

# retail_df = spark.read.jdbc(
#         jdbc_url,
#         'public.retail',
#         properties=jdbc_properties
# )

#     # # Simple aggregation (example: count by stock code)
#     # aggregated_df = retail_df.groupBy("stockcode").count()

#     # Output (example: write to console and CSV)
#     # aggregated_df.show()

#     # retail_df = spark.read.jdbc(
#     #     jdbc_url,
#     #     'retail',
#     #     properties=jdbc_properties
#     # )

#     # retail_df.xxshow()

# # if __name__ == "__main__":
# #     main()

# # spark = SparkSession.builder \
# #     .appName("PostgreSQL with JDBC") \
# #     .config("spark.jars", "/opt/postgresql-42.2.18.jar") \
# #     .getOrCreate()
# # # print(spark.read)
# # # print("hello world")

# # # JDBC connection properties
# # jdbc_url = "jdbc:postgresql://dataeng-postgres/postgres_db"
# # connection_properties = {
# #     "user": "user",
# #     "password": "password",
# #     "driver": "org.postgresql.Driver"
# # }

# # # Read from PostgreSQL
# # df = spark.read.jdbc(jdbc_url, "public.retail", properties=connection_properties)

# # jdbcDF2 = spark.read.jdbc("jdbc:postgresql://dataeng-postgres/postgres_db", "public.retail",
# #           properties={"user": "user", "password": "password"})
# # df.show()

import pyspark
from pyspark.sql import DataFrame

spark_host = "spark://dibimbing-dataeng-spark-master:7077"

sparkcontext = pyspark.SparkContext.getOrCreate(conf=(
        pyspark
        .SparkConf()
        .setAppName('retail-analysis')
        .setMaster('local')
        .set("spark.jars", "/opt/airflow/postgresql-42.2.18.jar")
    ))
sparkcontext.setLogLevel("WARN")

spark = pyspark.sql.SparkSession(sparkcontext.getOrCreate())

postgres_host = 'dataeng-postgres'
postgres_db = 'postgres_db'
postgres_user = 'user'
postgres_password = 'password'

jdbc_url = f'jdbc:postgresql://{postgres_host}/{postgres_db}'
# jdbc_url = "jdbc:postgresql://postgres:5432/airflow"
jdbc_properties = {
        'user': postgres_user,
        'password': postgres_password,
        'driver': 'org.postgresql.Driver',
        'stringtype': 'unspecified'
}

retail_df = spark.read.jdbc(
        jdbc_url,
        'public.retail',
        properties=jdbc_properties
)

retail_df.show()