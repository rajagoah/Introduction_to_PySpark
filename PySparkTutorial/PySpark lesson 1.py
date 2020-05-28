#this code will run only when run on the pyspark201 interpreter in pycharm
import pyspark
from pyspark.sql import SparkSession
import pandas as pd
import numpy as np

sc = pyspark.SparkContext("local","PySpark lesson 1")

#creating a spark session
spark = SparkSession.builder.getOrCreate()

#printing to console
print(spark)

#creating a pandas dataframe with 10 random numbers
df_temp = pd.DataFrame(np.random.random(10))

#creating a spark dataframe using the createDataFrame() method with the df_temp as the argument.
spark_temp = spark.createDataFrame(df_temp)
print(spark_temp.head())

#checking the list of tables in the catalog before adding the spark_temp to the catalog
if spark.catalog.listTables() == []:
    print('empty catalog')
else:
    print(spark.catalog.listTables())

#adding the spark_temp data frame to the catalog
spark_temp.createOrReplaceTempView('spark_temp')

#checking if the spark_temp data frame got added to the catalog
if spark.catalog.listTables() == []:
    print('empty catalog')
else:
    print(spark.catalog.listTables())


