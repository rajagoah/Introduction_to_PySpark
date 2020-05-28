from pyspark.sql import SparkSession
import pyspark
import pandas as pd
import numpy as np

#creating a data frame in pandas
df_temp = pd.DataFrame(np.random.random(10))

#creating a spark session, then converting the pandas dataframe to spark dataframe. Post that, adding to the catalog
spark = SparkSession.builder.getOrCreate()
spark_temp = spark.createDataFrame(df_temp)
spark_temp.createOrReplaceTempView('temp')
print(spark.catalog.listTables())

#querying using sql() function
query = 'From temp select *'

spark.sql(query).show()