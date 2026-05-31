from elasticsearch import Elasticsearch

try:
    # Connect to Elasticsearch
    es = Elasticsearch("http://localhost:9200")

    # Flight data document
    doc = {
        "source": "Paris",
        "destination": "London",
        "price": 150,
        "currency": "EUR"
    }

    # Insert data into Elasticsearch
    response = es.index(
        index="flight_prices",
        document=doc
    )

    print("Data inserted successfully!")
    print(response)

except Exception as e:
    print("Error occurred:")
    print(e)