struct1 = StructType().add("placeid", IntegerType(), True).add("placename", StringType(), True)
foodplaces = spark.read.schema (struct1).csv('/user/hadoop/foodplaces62216.txt')
foodplaces.printSchema()
foodplaces.show(5)