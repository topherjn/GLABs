import findspark
findspark.init()

from pyspark.sql import SparkSession
#and import struct types and data types
from pyspark.sql.types import StructType,StructField,StringType,IntegerType,FloatType
spark_app = SparkSession.builder.appName('sparkdemo').getOrCreate()

# ------create student data with 5 rows and 6 attributes------
students =[['001','john',23,5.79,67,'NY'], ['002','James',18,3.79,34,'NY'], ['003','Eric',17,2.79,17,'NJ'],
               ['004','Shahparan',19,3.69,28,'NJ'],['005','Flex',37,5.59,54,'Dallas']]

#----------define the StructType and StructFields-------
#for the below column names
schema=StructType([
    StructField("rollno",StringType(),True),
    StructField("name",StringType(),True),
    StructField("age",IntegerType(),True),
    StructField("height", FloatType(), True),
    StructField("weight", IntegerType(), True),
    StructField("address", StringType(), True)  ])
 
# #-----create the dataframe and add schema to the dataframe---
df = spark_app.createDataFrame(students, schema=schema)
print(df.schema)
print(df.schema.fields)
df.show()

df.printSchema()