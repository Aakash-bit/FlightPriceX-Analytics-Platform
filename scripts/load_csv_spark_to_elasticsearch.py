from pyspark.sql import SparkSession
from elasticsearch import Elasticsearch, helpers

# Create Spark Session
spark = SparkSession.builder \
    .appName("FlightPriceX") \
    .getOrCreate()

# Read CSV
df = spark.read.csv(
    r"E:\BigData_Project\data\flight_price.csv",
    header=True,
    inferSchema=True
)

print("Dataset Loaded")

df.show(5)

# Convert Spark DataFrame to Pandas
pandas_df = df.toPandas()

# Elasticsearch Connection
es = Elasticsearch("http://localhost:9200")

actions = []

for _, row in pandas_df.iterrows():
    actions.append({
        "_index": "flight_prices",
        "_source": row.to_dict()
    })

helpers.bulk(
    es,
    actions,
    chunk_size=500,
    request_timeout=300
)

print("Data Loaded Into Elasticsearch")

spark.stop()