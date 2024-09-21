# FraudDetect: Multi-Source Credit Card Fraud Detection

## Project Overview
<p align="justify">
The **MultiSource FraudBuster** project is designed to detect fraudulent credit card transactions using various data sources and machine learning techniques. The primary objective is to build an efficient fraud detection system that accurately identifies and prevents fraudulent activities. By integrating data from CSV files, web sources, and APIs, we aim to create a robust dataset that enhances the performance of the fraud detection model. Visualizations are also created to explore trends and patterns in fraud detection, providing insights into the underlying data and improving the detection system. The project is structured into several milestones, each focusing on different aspects of data preparation, transformation, and analysis to ensure a comprehensive approach to fraud detection.
</p>

## Table of Contents
- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Source Data](#source-data)
- [Milestones](#milestones)
  - [Milestone 1: Data Preparation and Integration](#milestone-1-data-preparation-and-integration)
  - [Milestone 2: Data Transformation and Cleaning (Flat File Source)](#milestone-2-data-transformation-and-cleaning-flat-file-source)
  - [Milestone 3: Data Transformation and Cleaning (Website Source)](#milestone-3-data-transformation-and-cleaning-website-source)
  - [Milestone 4: Data Transformation and Cleaning (API Source)](#milestone-4-data-transformation-and-cleaning-api-source)
  - [Milestone 5: Merging Data and Visualizing Trends](#milestone-5-merging-data-and-visualizing-trends)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## Installation
1. Ensure **Python 3.8** or above is installed. You can download it from [python.org](https://www.python.org/).
2. Install **PyCharm** (recommended for development).
3. Install the required packages

## Usage
1. Open the project in **PyCharm**.
2. Run the Python scripts to preprocess data, train models, and evaluate results.
3. Run the Python scripts to preprocess data, train models, and evaluate results.

## Data
The project utilizes several data sources related to credit card fraud detection, including transaction details, customer information, merchant information, and indicators of fraudulent activity.

### Source Data
- **API**: FraudLabs Pro API  
  This REST API detects all possible fraud traits based on the input parameters supplied. The more parameters supplied, the higher the accuracy of fraud detection.

- **CSV File**: [Credit Card Fraud Detection Dataset (Kaggle)](https://www.kaggle.com/datasets/shayannaveed/credit-card-fraud-detection)  
  A simulated dataset containing legitimate and fraudulent transactions from January 1, 2019, to December 31, 2020, covering credit cards of 1000 customers with a pool of 800 merchants.

- **CSV File**: [PaySim Synthetic Dataset (Kaggle)]([https://www.kaggle.com/ntnu-testimon/paysim1](https://www.kaggle.com/datasets/ealaxi/paysim1)  
  PaySim generates a synthetic dataset that resembles normal transaction operations while injecting malicious behavior to evaluate the performance of fraud detection methods.

- **Web**: [Synthetic Payments Data](https://datahub.io/machine-learning/creditcard/datapackage.json)  
  Data representing transactions from a subject-centric view, aimed at identifying fraudulent transactions. This dataset includes various transaction types representing normal and abnormal activities with predefined probabilities.

## Milestones

### Milestone 1: Data Preparation and Integration
- Integrated data from CSV files, web sources, and APIs to create a unified dataset for fraud detection.

### Milestone 2: Data Transformation and Cleaning (Flat File Source)
- Performed data cleaning and transformation on the CSV file, addressing missing values, formatting issues, and ensuring data consistency.

### Milestone 3: Data Transformation and Cleaning (Website Source)
- Fetched, cleaned, and transformed credit card data from a web source, standardizing formats and handling duplicates.

### Milestone 4: Data Transformation and Cleaning (API Source)
- Interfaced with the FraudLabs Pro API for real-time fraud validation and cleaned the API response data.

### Milestone 5: Merging Data and Visualizing Trends
- Merged the cleaned datasets into a SQLite database and created visualizations to explore trends and patterns in fraud detection.

## Future Work
Future improvements could include:
- Enhancing the model's accuracy and robustness.
- Incorporating additional data sources for better predictions.
- Developing a user-friendly interface for easier interaction with the fraud detection system.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgments
- [Kaggle](https://www.kaggle.com/)
- [Python](https://www.python.org/)
- [FraudLabs Pro](https://www.fraudlabspro.com/)
- [DataCamp](https://www.datacamp.com/)
- [Synthetic Payments Data](https://datahub.io/machine-learning/creditcard/datapackage.json)
