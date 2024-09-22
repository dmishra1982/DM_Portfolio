# Hotel Booking Optimizer using Big Data Approach

## Project Overview

<p align="justify">
The hotel industry is rapidly evolving, with Big Data playing a key role in transforming how hotels manage reservations. This project integrates Big Data analytics into hotel reservation management to address challenges like cancellations, optimize booking strategies, and enhance guest experiences. Using advanced analytical techniques, the project aims to predict cancellations, personalize guest experiences, and improve operational efficiency.
</p>

## Table of Contents
1. [Project Overview](#project-overview)
2. [Installation and Setup](#installation-and-setup)
3. [Codes and Resources Used](#codes-and-resources-used)
4. [Data](#data)
5. [Source Data](#source-data)
6. [Data Processing and Analysis](#data-processing-and-analysis)
7. [Results and Evaluation](#results-and-evaluation)
8. [Future Work](#future-work)
9. [Acknowledgments/References](#acknowledgmentsreferences)

## Installation and Setup

### Sign up for Google Cloud
- Visit the [Google Cloud](https://cloud.google.com) website.
- Click "Get Started for Free."
- Follow the prompts to create your account and receive $300 in credits.

### Create SSH Key
Generate an SSH key for secure access to the cloud instance:
  -  macOS: ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
  -  Windows: Use PuTTYgen to generate keys.

### Add SSH Key to Google Cloud
  -  Upload your public key to Google Cloud Console -> Compute Engine -> Metadata.

### Set up Ubuntu Instance
  -  Create Ubuntu 22.04 LTS instance with specified configurations.

### Start Big Data Software

  -  Navigate to relevant directories (hadoop-hive-spark-hbase, kafka, solr, nifi).
  -  Start services using Docker Compose: cd <directory-name> && docker-compose up -d

Remember to manage your Google Cloud credits and shut down instances when not in use.

## Codes and Resources Used
- Hadoop Distributed File System (HDFS) for data storage.
- Apache Hive for data organization and querying.
- Apache Spark for data processing and analysis.
- Apache Kafka for real-time data streaming.
- Apache NiFi for data ingestion.

## Data

The dataset used in this project consists of detailed hotel booking records, including various attributes such as:

- **Hotel Type**: The type of hotel (e.g., resort or city hotel).
- **Booking Status**: Whether the booking was completed, canceled, or pending.
- **Lead Time**: The number of days between the booking date and the arrival date.
- **Arrival Date**: The date on which the guest is scheduled to arrive.
- **Stay Duration**: The number of nights the guest is staying.
- **Guest Demographics**: Information such as age, gender, and country of origin.
- **Meal Type**: The type of meal plan selected by the guest.
- **Market Segment**: The segment (e.g., direct, corporate) through which the booking was made.
- **Distribution Channel**: The platform or channel used to make the booking.
- **Previous Cancellations**: The number of prior cancellations by the guest.
- **Room Type**: The type of room booked by the guest.

This comprehensive dataset provides key insights into reservation dynamics and customer behavior.

### Source Data

The dataset used for this project was sourced from [**Kaggle's Hotel Bookings Dataset**](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand). Make sure to download the dataset and place it in the appropriate directory within the project folder.

## Data Processing and Analysis

- **Data Ingestion with Apache NiFi**: Collect booking data from various channels in real-time.
- **Data Storage in HDFS**: Store the ingested data in a scalable and reliable manner.
- **Data Organization with Apache Hive**: Organize and structure data for easy querying and analysis.
- **Data Processing with Apache Spark**: Clean, transform, and analyze the data to extract actionable insights.
- **Real-Time Data Streaming with Apache Kafka**: Ensure continuous data flow for up-to-date analytics.

## Results and Evaluation

- Predictive models, particularly **logistic regression**, achieved an accuracy of **64.07%**.
- Analysis of booking patterns revealed valuable insights into guest behavior, lead times, and cancellation trends.

## Future Work

- Explore advanced machine learning techniques like **deep learning** and **ensemble models** to enhance prediction accuracy.
- Implement **Natural Language Processing (NLP)** for sentiment analysis on guest reviews.
- Integrate **Internet of Things (IoT)** data for real-time monitoring of hotel operations.
- Expand data sources to include **social media** and **web traffic** for comprehensive market analysis.

## Acknowledgments/References

- Kaggle
- 365 Data Science
- Python Plain English
- Journal of Big Data - Springer
- Towards Data Science
- Analytics Vidhya
- Machine Learning Mastery

