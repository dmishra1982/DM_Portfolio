# VitalFlow Guardian - Data-Powered Cardiac Risk Management

## Project Overview
<p align="justify">
  
**VitalFlow Guardian: Data-Powered Cardiac Risk Management** leverages electronic medical records and advanced machine learning techniques to predict and prevent heart failure. By analyzing a comprehensive dataset of patient records, including demographic information, medical history, and vital signs, this project aims to identify key risk factors and patterns associated with heart failure. The initiative represents a significant advancement in utilizing data-driven insights to enhance cardiovascular health and improve patient care.
</p>

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
To run the project locally, follow these steps:

1. **Clone the repository**:  
   Clone the GitHub repository to your local machine using Git.

2. **Set up Anaconda environment**:  
   Create and activate a new Anaconda environment with Python 3.8.

3. **Install dependencies**:  
   Install the required Python packages listed in `requirements.txt`.

4. **Download the dataset**:  
   Download the dataset required for the project and place it in the designated directory.

## Usage
To reproduce the analysis and results:

1. **Run the Jupyter notebooks**:
   - Navigate to and open the Jupyter notebooks.

2. **Follow the notebooks for EDA and modeling**:
   - Perform **Exploratory Data Analysis (EDA)** to understand data patterns.
   - Model training and evaluation using **Logistic Regression**, **Decision Trees**, and **Random Forest**.

3. **Explore results**:
   - Review the generated plots, metrics, and insights from the notebooks.

## Data
The dataset contains **319,795 entries** and **18 columns**, covering demographic and clinical factors related to heart health.

### Source Data
The dataset used for this project is sourced from the **Heart Failure Dataset**.

## Model Training and Evaluation
The project utilizes the following machine learning models for heart failure prediction:
- **Logistic Regression**
- **Decision Trees**
- **Random Forest**
- **XGBoost (Extreme Gradient Boosting)**
- **Gradient Boosting Machine (GBM)**

Evaluation metrics include:
- Accuracy
- Precision
- Recall
- F1-score
- ROC AUC

Cross-validation and confusion matrices are used to assess model performance.

## Results
The **Random Forest Classifier** achieved an accuracy of **98%**, with high precision and recall scores, demonstrating effective heart failure prediction capabilities.

## Future Work
Potential future enhancements include:
- Implementing **deep learning models** for more complex pattern recognition.
- Incorporating **real-time data streaming** for continuous heart health monitoring.
- Developing a **web application** for interactive heart health analytics.

## Acknowledgments
This project acknowledges contributions from various datasets and research studies that facilitated comprehensive heart failure analysis and prediction:
- [Heart Failure Dataset on Kaggle](https://www.kaggle.com/)
- [UCI Heart Failure Clinical Records](https://archive.ics.uci.edu/)
- [IEEE Xplore Heart Failure Dataset](https://ieeexplore.ieee.org/)
- [NHS Scotland Heart Failure Dataset](https://www.isdscotland.org/)
- [ScienceDirect Heart Failure Dataset](https://www.sciencedirect.com/)
- [BioMed Central Heart Failure Dataset](https://bmcpublichealth.biomedcentral.com/)
- [NHLBI Heart Failure Research](https://www.nhlbi.nih.gov/)
- [AHA Journals Heart Failure Research](https://www.ahajournals.org/)
