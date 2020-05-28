from pyspark import SparkContext
from pyspark.sql import SparkSession

#creating a spark context
sc = SparkContext("local","PySpark lesson 1")

#printing to console
print(sc)

#creating a pyspark session instance
my_spark = SparkSession.builder.getOrCreate()

#printing to console
print(my_spark)