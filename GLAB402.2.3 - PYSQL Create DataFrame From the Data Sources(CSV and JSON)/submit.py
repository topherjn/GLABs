import pyspark
from pyspark.sql import SparkSession #Importing the Libraries
from pyspark.sql.types import StructType,StructField, StringType, IntegerType,BooleanType,DoubleType

# make the cars data easier to reference
data = 'D:\Per Scholas\SparkStuff\data'

# Creating Spark Session
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
# Reading /loading the Dataset from CSV file
cardf = spark.read.load(f"{data}\{'cars.csv'}", format="csv", header = True,inferSchema = True)

# the types of the columns
cardf.printSchema()

# column names
for column in cardf.columns:
    print(column)

# whole dataset (well, 20 columns)
cardf.show()

# top of the set
print(cardf.head())

# end of set
print(cardf.tail(2))

# number of columns
print(len(cardf.columns))

# get statistics for Car column
cardf.describe('Car').show()

# sort by acceleration
cardf.orderBy(cardf.Acceleration.desc()).show(10)

# task 2

# Read JSON file into dataframe into dataframe:
df = spark.read.json(f"{data}\{'zipcode.json'}")
df.printSchema()
df.show()

# Read multi-line JSON file into dataframe:
multiline_df = spark.read.option("multiline","true") \
      .json(f"{data}\{'multiline-zipcode.json'}")
multiline_df.show()

# Read multiple JSON files into dataframe:
df2 = spark.read.json([f"{data}\{'zipcode.json'}",f"{data}\{'zipcode1.json'}"])
df2.show(4)   

# Read all JSON files from a directory:
df3 = spark.read.json(f"{data}\*.json")
df3.show()

schema = StructType([
      StructField("RecordNumber",IntegerType(),True),
      StructField("Zipcode",IntegerType(),True),
      StructField("ZipCodeType",StringType(),True),
      StructField("City",StringType(),True),
      StructField("State",StringType(),True),
      StructField("LocationType",StringType(),True),
      StructField("Lat",DoubleType(),True),
      StructField("Long",DoubleType(),True),
      StructField("Xaxis",IntegerType(),True),
      StructField("Yaxis",DoubleType(),True),
      StructField("Zaxis",DoubleType(),True),
      StructField("WorldRegion",StringType(),True),
      StructField("Country",StringType(),True),
      StructField("LocationText",StringType(),True),
      StructField("Location",StringType(),True),
      StructField("Decommisioned",BooleanType(),True),
      StructField("TaxReturnsFiled",StringType(),True),
      StructField("EstimatedPopulation",IntegerType(),True),
      StructField("TotalWages",IntegerType(),True),
      StructField("Notes",StringType(),True)
  ])

# custom schema
df_with_schema = spark.read.schema(schema).json(f"{data}\zipcode.json")
df_with_schema.printSchema()
df_with_schema.show(3)


spark.stop()
