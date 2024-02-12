from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from srujantestpipeline.config.ConfigStore import *
from srujantestpipeline.udfs.UDFs import *

def SrujantestDataset(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("emp_id", StringType(), True), StructField("name", StringType(), True), StructField("salary", StringType(), True), StructField("address", StringType(), True), StructField("loc", StringType(), True), StructField("email", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/FileStore/srujandev/emp_1.csv")
