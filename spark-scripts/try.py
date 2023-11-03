import sys
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

from pyspark.sql.window import Window
from pyspark.sql.functions import rank

# Create spark session
spark = (SparkSession
    .builder
    .getOrCreate()
)

print("######################################")
print("READING POSTGRES TABLES")
print("######################################")

retail_df = (
    spark.read
    .format("jdbc")
    .option("url", "jdbc:postgresql://dataeng-postgres/postgres_db")
    .option("dbtable", "public.retail")
    .option("user", "user")
    .option("password", "password")
    .load()
)

# df_movies.show()

# Assuming data is loaded into a DataFrame named retail_df
retail_df = retail_df.withColumn("invoicedate", F.to_date("invoicedate", "yyyy-MM-dd"))

# Calculate the maximum purchase date for each customer
max_purchase_date = retail_df.groupBy("customerid").agg(F.max("invoicedate").alias("last_purchase_date"))

# Let's assume a customer who hasn't made a purchase in the last 30 days is considered churned
churned_customers = max_purchase_date.filter(F.datediff(F.current_date(), "last_purchase_date") > 30)

# For return analysis, we would observe these churned customers in the subsequent period. 
# This involves more complex logic such as observing their next purchase date after the churn date, etc.

# For this example, let's just count the number of churned customers
churned_count = churned_customers.count()

print("######################################")
print("let's just count the number of churned customers, we would observe these churned customers in the subsequent period")
print("######################################")
print(f"Number of churned customers: {churned_count}")

windowSpec = Window.orderBy(retail_df["quantity"].desc())
# We want to rank each product based on the quantity sold:
ranked_df = retail_df.withColumn("rank", rank().over(windowSpec))
print("######################################")
print("RANK EACH PRODUCT BASED ON THE QUANTITY SOLD")
print("######################################")
print(ranked_df.show())