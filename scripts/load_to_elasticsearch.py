from elasticsearch import Elasticsearch, helpers
import pandas as pd
import os

# Project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# CSV path
csv_path = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "final_flight_fuel.csv"
)

# Load CSV
df = pd.read_csv(csv_path)

print("Dataset Loaded")
print("Rows:", len(df))

# Connect to Elasticsearch
es = Elasticsearch("http://localhost:9200")

# Check connection
if not es.ping():
    raise ValueError("Could not connect to Elasticsearch")

print("Connected to Elasticsearch")

index_name = "flight_fuel_data"

# Delete existing index (optional)
if es.indices.exists(index=index_name):
    es.indices.delete(index=index_name)

# Create index
es.indices.create(index=index_name)

print(f"Index '{index_name}' created")

# Bulk insert
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