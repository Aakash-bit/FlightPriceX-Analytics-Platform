# FlightPriceX Analytics Platform

## Overview

FlightPriceX Analytics Platform is a Big Data analytics project developed to examine flight ticket prices and generate meaningful business insights. The project combines flight fare data with fuel price information and processes it through a complete end-to-end analytics pipeline.

The solution was built using Python, Elasticsearch, Kibana, Docker, Apache Airflow, and Machine Learning techniques. The main objective of the project is to demonstrate how modern data engineering and analytics technologies can be utilized to process large datasets and support data-driven decision-making.

---

## Project Objectives

The primary objectives of this project are:

- Analyze flight ticket pricing patterns and trends.
- Integrate external fuel price information into the analysis.
- Develop a scalable ETL pipeline.
- Store processed data in Elasticsearch.
- Build interactive dashboards using Kibana.
- Explore predictive analytics through Machine Learning.

---

## Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Data Processing and Automation |
| Pandas | Data Cleaning and Transformation |
| Apache Airflow | Workflow Orchestration |
| Elasticsearch | Data Storage and Search |
| Kibana | Dashboard Visualization |
| Docker | Containerized Deployment |
| PostgreSQL | Airflow Metadata Database |
| Scikit-Learn | Machine Learning |
| GitHub | Version Control |

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

The flight dataset contains more than 300,000 flight records and includes the following attributes:

- Airline
- Source City
- Destination City
- Departure Time
- Arrival Time
- Stops
- Travel Class
- Duration
- Days Left Before Departure
- Ticket Price

### Fuel Data

Fuel price information was incorporated as an external economic indicator to enrich the analysis and demonstrate the integration of multiple data sources.

---

## ETL Pipeline

The project follows a standard ETL (Extract, Transform, Load) workflow.

### Extract

- Load flight data from CSV files.
- Gather fuel price information from an external source.

### Transform

- Clean and preprocess the data.
- Remove unnecessary fields.
- Merge the flight and fuel datasets.
- Generate a final processed dataset.

### Load

- Store processed records in Elasticsearch.
- Create searchable indexes for analytics and visualization purposes.

---

## Elasticsearch Integration

The processed data is indexed into Elasticsearch using a dedicated index:

```text
flight_fuel_data
```

Key benefits include:

- Fast query performance
- Real-time analytics capabilities
- Scalability for large datasets
- Seamless integration with Kibana

---

## Kibana Dashboard

The dashboard offers a variety of KPI cards and visualizations.

### KPI Cards

- Average Fuel Price
- Total Flights
- Average Flight Price
- Maximum Flight Price
- Minimum Flight Price

### Visualizations

- Average Flight Price by Airline
- Average Price by Source City
- Average Price by Destination City
- Flight Class Distribution
- Price Trend by Days Left Before Departure
- Average Flight Duration by Airline

---

## Key Insights

Some significant findings from the analysis include:

- Flight ticket prices generally increase as the departure date gets closer.
- Premium airlines tend to have higher average ticket prices.
- Business-class fares are significantly more expensive than Economy-class fares.
- Ticket prices vary considerably across different cities and airlines.
- Fuel price information can be integrated into airfare analytics for future forecasting applications.

---

## Machine Learning Extension

A Random Forest Regression model was explored to predict flight ticket prices.

### Features Used

- Airline
- Source City
- Destination City
- Travel Class
- Duration
- Days Left Before Departure
- Fuel Price

### Target

- Flight Ticket Price

This extension enables the project to evolve from descriptive analytics to predictive analytics.

---

## Challenges Faced

Several challenges were encountered during development, including:

- Integrating external fuel price data
- Indexing large datasets in Elasticsearch
- Configuring and orchestrating workflows with Airflow
- Setting up the Docker environment
- Managing large-scale data processing

Addressing these challenges provided valuable experience in real-world data engineering and analytics workflows.

---

## Future Enhancements

Potential future improvements include:

- Real-time flight fare monitoring
- Historical fuel price integration
- Apache Kafka streaming architecture
- Advanced machine learning models
- Cloud deployment using AWS or Azure
- Real-time predictive dashboards

---

## Conclusion

FlightPriceX Analytics Platform demonstrates how Big Data technologies can be applied to analyze airline ticket pricing and generate actionable business insights. By combining flight fare and fuel price data, the project showcases a complete analytics workflow that includes data ingestion, processing, storage, visualization, and predictive analytics.

This project highlights the practical application of Python, Airflow, Elasticsearch, Kibana, Docker, and Machine Learning in solving real-world analytics challenges.

---

## Author

**Aakash M**

**Jithesh kumar**

Master's Student – Big Data & Artificial Intelligence

GitHub Repository:

https://github.com/Aakash-bit/FlightPriceX-Analytics-Platform
