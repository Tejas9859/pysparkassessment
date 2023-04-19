from pyspark.sql import SparkSession
import main

if __name__ == "__main__":
    spark = SparkSession.builder.appName("MyApp").getOrCreate()
    main.run(spark)
    spark.stop()
