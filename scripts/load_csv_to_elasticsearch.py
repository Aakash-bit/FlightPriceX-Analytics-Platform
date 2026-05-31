import pandas as pd
from elasticsearch import Elasticsearch, helpers

es = Elasticsearch("http://localhost:9200")

df = pd.read_csv(r"E:\BigData_Project\data\flight_price.csv")

df = df.fillna("Unknown")

print("CSV Loaded Successfully")

index_name = "flight_prices"

actions = []

for _, row in df.iterrows():
    actions.append({
        "_index": index_name,
        "_source": row.to_dict()
    })

# Send in smaller chunks
helpers.bulk(
    es,
    actions,
    chunk_size=1000,
    request_timeout=120
)

print("Data uploaded successfully!")