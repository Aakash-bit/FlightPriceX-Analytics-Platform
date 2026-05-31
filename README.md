# FlightPriceX Analytics Platform

## Overview

FlightPriceX Analytics Platform is a Big Data and Data Engineering project designed to collect, process, analyze, and visualize flight pricing data in real time. The platform leverages modern data engineering tools such as Apache Airflow, Apache Spark, Elasticsearch, Kibana, Docker, and Python to build an end-to-end analytics pipeline.

The system automates data ingestion, performs data transformation and cleaning, stores processed data efficiently, and provides interactive dashboards for monitoring flight price trends and analytics.

---

## Project Architecture

1. **Data Ingestion**

   * Collects flight pricing data from APIs or datasets.
   * Automated using Apache Airflow DAGs.

2. **Data Processing**

   * Apache Spark performs data cleaning, transformation, and aggregation.
   * Generates analytics-ready datasets.

3. **Data Storage**

   * Processed data is indexed into Elasticsearch.
   * Enables fast querying and search capabilities.

4. **Visualization**

   * Kibana dashboards provide real-time analytics.
   * Displays flight trends, pricing patterns, and KPIs.

---

## Technologies Used

* Python
* Apache Airflow
* Apache Spark
* Elasticsearch
* Kibana
* Docker & Docker Compose
* Pandas
* REST APIs
* Git & GitHub

---

## Key Features

* Automated ETL Pipeline
* Real-Time Data Processing
* Flight Price Trend Analysis
* Interactive Kibana Dashboards
* KPI Monitoring
* Dockerized Deployment
* Scalable Big Data Architecture

---

## KPI Metrics

The platform tracks the following business metrics:

* Average Flight Price
* Maximum Flight Price
* Minimum Flight Price
* Total Flights Processed
* Average Price by Airline
* Average Price by Route
* Price Trend Over Time
* Flight Volume Analysis

---

## Project Structure

```text
FlightPriceX-Analytics-Platform/
│
├── airflow/
│   ├── dags/
│   ├── logs/
│   └── plugins/
│
├── scripts/
│   ├── ingestion.py
│   ├── transformation.py
│   └── elasticsearch_loader.py
│
├── docker-compose.yml
├── requirements.txt
├── BigData_Report.docx
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/FlightPriceX-Analytics-Platform.git
cd FlightPriceX-Analytics-Platform
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start Services

```bash
docker-compose up -d
```

### Access Applications

| Service       | URL                   |
| ------------- | --------------------- |
| Airflow       | http://localhost:8080 |
| Kibana        | http://localhost:5601 |
| Elasticsearch | http://localhost:9200 |

---

## Dashboard Insights

The Kibana dashboard provides:

* Flight Price Trends
* Airline-wise Analysis
* Route Performance
* Price Distribution
* Top Expensive Routes
* Cheapest Travel Destinations
* Daily Flight Monitoring

---

## Future Enhancements

* Machine Learning Price Prediction
* Real-Time Streaming with Kafka
* Cloud Deployment (AWS/Azure/GCP)
* Automated Alerting System
* Advanced Forecasting Models

---

## Author

**Aakash Muthuselvan**

Master's Student – Big Data & Analytics

---

## License

This project is developed for academic and educational purposes.

<img width="1600" height="559" alt="WhatsApp Image 2026-05-31 at 4 22 57 PM" src="https://github.com/user-attachments/assets/66aee8a2-c152-4e14-a6b3-6570b1c86d3e" />
