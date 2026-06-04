# FlightPriceX Analytics Platform

## Overview

FlightPriceX Analytics Platform is a Big Data analytics project developed to analyze flight ticket prices and generate meaningful business insights. The project combines flight fare data with fuel price information and processes the data through an end-to-end analytics pipeline.

The solution was built using Python, Elasticsearch, Kibana, Docker, Apache Airflow, and Machine Learning techniques. The goal of the project is to demonstrate how modern data engineering and analytics tools can be used to process large datasets and support data-driven decision making.

---

## Project Objectives

The main objectives of this project are:

* Analyze flight ticket pricing patterns.
* Integrate external fuel price information.
* Build a scalable ETL pipeline.
* Store processed data in Elasticsearch.
* Create interactive dashboards using Kibana.
* Explore predictive analytics using Machine Learning.

---

## Technologies Used

| Technology     | Purpose                          |
| -------------- | -------------------------------- |
| Python         | Data Processing and Automation   |
| Pandas         | Data Cleaning and Transformation |
| Apache Airflow | Workflow Orchestration           |
| Elasticsearch  | Data Storage and Search          |
| Kibana         | Dashboard and Visualization      |
| Docker         | Containerized Deployment         |
| PostgreSQL     | Airflow Metadata Database        |
| Scikit-Learn   | Machine Learning                 |
| GitHub         | Version Control                  |

---

## Project Architecture

```text
Flight Dataset (CSV)
          +
Fuel Price Data
          ↓
     ETL Pipeline
          ↓
    Elasticsearch
          ↓
       Kibana
          ↓
 Business Insights
          ↓
 Machine Learning
```

---

## Dataset Information

### Flight Dataset

The flight dataset contains more than 300,000 flight records and includes:

* Airline
* Source City
* Destination City
* Departure Time
* Arrival Time
* Stops
* Travel Class
* Duration
* Days Left Before Departure
* Ticket Price

### Fuel Data

Fuel price information was integrated as an external economic indicator to enrich the analysis and demonstrate multi-source data integration.

---

## ETL Pipeline

The project follows a standard ETL (Extract, Transform, Load) workflow.

### Extract

* Load flight data from CSV files.
* Collect fuel price information from an external source.

### Transform

* Clean and preprocess data.
* Remove unnecessary fields.
* Merge flight and fuel datasets.
* Generate a final processed dataset.

### Load

* Store processed records in Elasticsearch.
* Create searchable indexes for analytics and visualization.

---

## Elasticsearch Integration

Processed data is indexed into Elasticsearch using a dedicated index:

```text
flight_fuel_data
```

Benefits include:

* Fast querying
* Real-time analytics
* Scalability
* Seamless Kibana integration

---

## Kibana Dashboard

The dashboard provides several KPI cards and visualizations.

### KPI Cards

* Average Fuel Price
* Total Flights
* Average Flight Price
* Maximum Flight Price
* Minimum Flight Price

### Visualizations

* Average Flight Price by Airline
* Average Price by Source City
* Average Price by Destination City
* Flight Class Distribution
* Price Trend by Days Left
* Average Flight Duration by Airline

---

## Key Insights

Some important findings from the analysis include:

* Flight prices generally increase as the departure date approaches.
* Premium airlines tend to have higher average ticket prices.
* Business-class tickets are significantly more expensive than Economy-class tickets.
* Ticket prices vary considerably across cities and airlines.
* Fuel price information can be integrated into airfare analytics for future forecasting studies.

---

## Machine Learning Extension

A Random Forest Regression model was explored to predict flight ticket prices.

### Features Used

* Airline
* Source City
* Destination City
* Travel Class
* Duration
* Days Left Before Departure
* Fuel Price

### Target

* Flight Ticket Price

This extension transforms the project from descriptive analytics into predictive analytics.

---

## Challenges Faced

During development, several challenges were encountered:

* Integration of external fuel price data
* Elasticsearch indexing of large datasets
* Airflow configuration and orchestration
* Docker environment setup
* Managing large-scale data processing

These challenges provided valuable experience in real-world data engineering workflows.

---

## Future Enhancements

Potential improvements include:

* Real-time flight fare monitoring
* Historical fuel price integration
* Apache Kafka streaming architecture
* Advanced machine learning models
* Cloud deployment using AWS or Azure
* Real-time predictive dashboards

---

## Conclusion

FlightPriceX Analytics Platform demonstrates how Big Data technologies can be applied to analyze airline ticket pricing and generate actionable insights. By integrating flight fare and fuel price data, the project showcases a complete analytics workflow including data ingestion, processing, storage, visualization, and predictive analytics.

This project highlights the practical use of Python, Airflow, Elasticsearch, Kibana, Docker, and Machine Learning in solving real-world analytics problems.

---

## Author

**Aakash M**

Master's Student – Big Data & Artificial Intelligence

GitHub Repository:
https://github.com/Aakash-bit/FlightPriceX-Analytics-Platform
