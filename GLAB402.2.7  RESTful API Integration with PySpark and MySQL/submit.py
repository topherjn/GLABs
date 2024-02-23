import findspark
findspark.init()
import pyspark
from pyspark.sql import SparkSession
import requests

# Initialize SparkSaession
spark = SparkSession.builder \
    .appName("Read and Save JSON Data with PySpark SQL") \
    .getOrCreate()

# API Endpoint URL
api_url = "https://jsonplaceholder.typicode.com/posts/"

# Fetch data from API
response = requests.get(api_url)
if response.status_code == 200:
    # Convert JSON response to DataFrame
    json_df = spark.read.json(spark.sparkContext.parallelize([response.json()]))
    
    # Show DataFrame schema and content
    json_df.printSchema()
    json_df.show()

    # Define MySQL connection properties
    mysql_props = {
        "user": "root",
        "password": "password",
        "driver": "com.mysql.cj.jdbc.Driver"
    }
    # JDBC URL for MySQL
    mysql_url = "jdbc:mysql://localhost:3306/classicmodels"
    # Save DataFrame to MySQL table
    json_df.write \
        .jdbc(url=mysql_url, table="json_data_table", mode="overwrite", properties=mysql_props)
else:
    print(f"Failed to fetch data from API. Status code: {response.status_code}")
# Stop SparkSession
spark.stop()