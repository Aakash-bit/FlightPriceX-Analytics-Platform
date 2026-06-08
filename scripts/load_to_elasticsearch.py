from elasticsearch import Elasticsearch, helpers
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

csv_path = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "final_flight_fuel.csv"
)

df = pd.read_csv(csv_path)

print("Dataset Loaded")
print("Rows:", len(df))

es = Elasticsearch("http://localhost:9200")

if not es.ping():
    raise ValueError("Could not connect to Elasticsearch")

print("Connected to Elasticsearch")

index_name = "flight_fuel_data"

# Delete existing index (optional)
if es.indices.exists(index=index_name):
    es.indices.delete(index=index_name)

es.indices.create(index=index_name)

print(f"Index '{index_name}' created")

actions = []

for _, row in df.iterrows():
    actions.append({
        "_index": index_name,
        "_source": row.to_dict()
    })

helpers.bulk(es, actions)

print(f"{len(df)} records loaded successfully!")

# Verify count
count = es.count(index=index_name)

print("Documents in Elasticsearch:")
print(count["count"])