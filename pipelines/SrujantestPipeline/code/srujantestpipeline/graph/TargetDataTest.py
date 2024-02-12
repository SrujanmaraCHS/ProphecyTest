from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from srujantestpipeline.config.ConfigStore import *
from srujantestpipeline.udfs.UDFs import *

def TargetDataTest(spark: SparkSession, in0: DataFrame):
    in0.write\
        .option("header", True)\
        .option("sep", ",")\
        .mode("overwrite")\
        .option("separator", ",")\
        .option("header", True)\
        .csv("dbfs:/FileStore/srujandev/testprophecy/_temp")
    from prophecy.utils.gems_utils import concatenateFiles
    concatenateFiles(
        spark,
        ".csv",
        "overwrite",
        "dbfs:/FileStore/srujandev/testprophecy/_temp",
        "dbfs:/FileStore/srujandev/testprophecy/",
        True,
        True
    )
