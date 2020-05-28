#this code will run only when run on the pyspark201 interpreter in pycharm
import pyspark
from pyspark.sql import SparkSession

sc = pyspark.SparkContext("local","PySpark lesson 1")

#creating a spark session
spark = SparkSession.builder.getOrCreate()

#printing to console
print(spark)

#viewing the tables within the spark context
print(spark.catalog.listTables())