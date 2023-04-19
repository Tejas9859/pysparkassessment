from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("MyApp").getOrCreate()

# Read the CSV file
df = spark.read.format("csv").option("header", "true").load(r"C:\Users\LENOVO\Desktop\jupyter_notebook\categories.csv")

# Write the result to a Parquet file
df2=df.write.format("parquet").save(r"C:\Users\LENOVO\Desktop\jupyter_notebook\categories_output.csv")

# Stop the SparkSession
spark.stop()
