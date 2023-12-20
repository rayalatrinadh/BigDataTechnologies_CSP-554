# PySpark shell
from pyspark.sql.types import *

# Define the schema
schema1 = StructType([
    StructField("name", StringType(), True),
    StructField("food1", IntegerType(), True),
    StructField("food2", IntegerType(), True),
    StructField("food3", IntegerType(), True),
    StructField("food4", IntegerType(), True),
    StructField("placeid", IntegerType(), True)
])

# Load the CSV file
foodratings = spark.read.csv("/user/hadoop/foodratings62216.txt", schema=schema1, header=True)

# Print the schema
foodratings.printSchema()

# Show the first 5 rows
foodratings.show(5)