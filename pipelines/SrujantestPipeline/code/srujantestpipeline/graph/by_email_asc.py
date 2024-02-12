from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from srujantestpipeline.config.ConfigStore import *
from srujantestpipeline.udfs.UDFs import *

def by_email_asc(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.orderBy(col("salary").asc())
