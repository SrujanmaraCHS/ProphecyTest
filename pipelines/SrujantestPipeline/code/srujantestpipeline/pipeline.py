from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from srujantestpipeline.config.ConfigStore import *
from srujantestpipeline.udfs.UDFs import *
from prophecy.utils import *
from srujantestpipeline.graph import *

def pipeline(spark: SparkSession) -> None:
    df_SrujantestDataset = SrujantestDataset(spark)
    df_by_email_asc = by_email_asc(spark, df_SrujantestDataset)
    TargetDataTest(spark, df_by_email_asc)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/SrujantestPipeline")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/SrujantestPipeline", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/SrujantestPipeline")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
