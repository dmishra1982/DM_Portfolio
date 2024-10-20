# CreditGuard -  Credit Card Fraud Detection & Prevention

## Project Overview

Credit card fraud is a significant issue for organizations, consumers, banks, and merchants, leading to financial losses and eroding trust. This project aims to develop a robust fraud detection system using machine learning and data mining techniques in **R** . By employing **Logistic Regression** and **Random Forest Classifier** models, the system analyzes purchase data to detect inconsistencies and swiftly identify fraud. The success of the project is measured by the accuracy of fraud detection, ensuring a reliable and effective solution to this critical problem.


## Table of Contents
1. [Project Overview](#project-overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Data](#data)
5. [Source Data](#source-data)
6. [Model Training and Evaluation](#model-training-and-evaluation)
7. [Results](#results)
8. [Future Work](#future-work)
9. [Acknowledgments](#acknowledgments)

## Installation
To set up the project environment, follow these steps:

1. **Install Anaconda**:  
   Download and install Anaconda from [Anaconda's official website](https://www.anaconda.com/products/individual).

2. **Open Anaconda Navigator**:  
   Launch Anaconda Navigator from your application menu or command line.

3. **Open Jupyter Notebook**:  
   Click on the Jupyter Notebook icon in Anaconda Navigator to open it in your web browser.

4. **Create or Open a Notebook**:  
   Create a new notebook or open an existing one to start working with Python.

## Usage
To use the project, follow these steps:

1. **Prepare your dataset**:  
   Ensure your dataset is structured according to the guidelines provided in the [Data](#data) section.

2. **Train and evaluate models**:  
   Train the **Logistic Regression** and **Random Forest Classifier** models as described in the [Model Training and Evaluation](#model-training-and-evaluation) section.

3. **Analyze results**:  
   Review the performance of the models in the [Results](#results) section and plan future enhancements in the [Future Work](#future-work) section.

## Data
The dataset consists of simulated credit card transactions spanning from January 2019 to December 2020, covering 1000 customers and 800 merchants. This data includes transaction details such as amount, merchant ID, customer ID, and fraud labels.

### Source Data
The dataset used in this project is sourced from the **Credit Card Transactions Fraud Detection Dataset** on Kaggle.

## Model Training and Evaluation
The project employs the following machine learning models:

- **Logistic Regression**
- **Random Forest Classifier**

Model performance is evaluated based on **accuracy**, with results validated against a holdout test set. Additional metrics such as **precision** and **recall** can be incorporated for further analysis.

## Results
- **Logistic Regression Model**: Achieved very good accuracy in detecting fraudulent transactions.
- **Random Forest Classifier**: Outperformed the Logistic Regression model with an accuracy of 95+ %, demonstrating superior fraud detection capabilities.

## Future Work
Potential future enhancements for the project include:

- **Improving model robustness**: Address the issue of imbalanced datasets to improve detection rates for minority classes.
- **Real-time fraud detection**: Implement real-time fraud detection to immediately flag suspicious transactions.
- Exploring ensemble methods for model improvement.
  
## Acknowledgments
- Kaggle for providing the Credit Card Transactions Fraud Detection Dataset.
- The [R](https://www.r-project.org/) community for the powerful libraries used in data analysis and machine learning.
- Analytical Vidhya for insightful resources and tutorials on machine learning techniques.
- [Towards Data Science](https://towardsdatascience.com/) 

