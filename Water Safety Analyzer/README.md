# Water Safety Analyzer 

## Project Overview
<p align="justify">
The project develops a predictive model to assess water potability using historical water quality data. Various parameters such as pH, hardness, and contamination levels are analyzed to predict whether water is safe for consumption. This project supports public health initiatives by providing actionable insights to ensure safe drinking water.
</p>

## Table of Contents
1. [Project Overview](#project-overview)
2. [Installation and Setup](#installation-and-setup)
3. [Python Packages Used](#python-packages-used)
4. [Data Source](#data-source)
5. [Results and Evaluation](#results-and-evaluation)
6. [Future Work](#future-work)
7. [Acknowledgments/References](#acknowledgmentsreferences)

## Installation and Setup

1. **Install Anaconda**: Download and install Anaconda from the [official Anaconda website](https://www.anaconda.com/products/individual).
2. **Open Anaconda Navigator**: Launch Anaconda Navigator from your application menu or command line.
3. **Open Jupyter Notebook**: Click on the Jupyter Notebook icon in the Anaconda Navigator to open it in your web browser.
4. **Create or Open a Notebook**: Create a new notebook or open an existing one to start working with Python.

## Python Packages Used

The following Python packages are used in this project:

- `pandas` - For data manipulation and analysis
- `numpy` - For numerical computations
- `scikit-learn` - For machine learning algorithms and evaluation metrics
- `matplotlib` - For data visualization
- `seaborn` - For statistical data visualization
- `catboost` - For gradient boosting
- `lightgbm` - For gradient boosting
- `xgboost` - For gradient boosting

## Data Source

The dataset used in this project can be accessed on Kaggle and includes water quality metrics for 3,276 different water samples. Each sample is assessed for various parameters such as pH, hardness, solids, chloramines, sulfate, conductivity, organic carbon, trihalomethanes, and turbidity. The dataset also includes a binary target variable indicating water potability.

- [Safe Aquifers Dataset on Kaggle](https://www.kaggle.com/adityakadiwal/water-potability)

Ensure you download the dataset and place it in the appropriate directory within the project folder.

## Results and Evaluation

<p align="justify">
This project evaluated several machine learning models, including Random Forest, XGBoost, and LightGBM. Key results include:
</p>
<p align="justify">
Overall, Random Forest emerged as the top-performing model, excelling in accuracy, AUC, precision, and F1 score, along with a high Kappa coefficient and MCC. XGBoost demonstrated strong performance, particularly in recall and MCC. CatBoost, despite its longer training time, performed well in accuracy and AUC. KNN, while the fastest, had lower overall performance metrics.
</p>
<p align="justify">
The hyperparameter tuning and evaluation of four machine learning models—Random Forest, CatBoost, LightGBM, and XGBoost—yielded insightful results regarding their performance on the test dataset. Random Forest achieved an accuracy of 71.60% with its best parameters set to max_depth of 10, max_features as None, min_samples_leaf of 2, min_samples_split of 10, and n_estimators of 200. The model displayed a precision of 72% for class 0 and 71% for class 1, with a recall of 68% and 75% respectively. The classification report indicated that while Random Forest effectively identified instances of class 1, it struggled slightly with class 0, reflected in the lower recall rate.
</p>
<p align="justify">
CatBoost outperformed Random Forest with an accuracy of 73.09%. Its optimal parameters included a depth of 8, iterations of 200, l2_leaf_reg of 5, and a learning_rate of 0.05. The model maintained strong performance with precision and recall values close to 73% for both classes. This balance illustrates CatBoost's effectiveness in handling imbalanced data while achieving reliable classification results across both classes.
</p>
<p align="justify">
LightGBM recorded an accuracy of 72.35%, supported by best parameters of learning_rate at 0.01, max_depth of 30, n_estimators at 300, and `num_leaves** of 31. The precision and recall values were similarly balanced, reflecting its capability to generalize well on the dataset. LightGBM performed slightly better than Random Forest, demonstrating its potential as a robust model for this classification task. 
</p>
<p align="justify">
XGBoost emerged as the top performer with an accuracy of 74.69%. The optimal hyperparameters included a learning_rate of 0.1, max_depth of 10, n_estimators of 100, and a subsample rate of 0.9. It showed commendable precision of 74% for class 0 and 76% for class 1, along with robust recall values of 74% and 75%. The overall performance of XGBoost indicates its efficiency in not only fitting the training data but also effectively predicting unseen data.
</p>

## Future Work

- **Expand the Dataset**: Incorporate samples from more diverse regions to improve model generalizability.
- **Model Enhancement**: Explore advanced techniques and hyperparameter tuning to further enhance model performance.
- **Integration**: Implement the predictive model into water treatment facilities for real-time monitoring and early detection of contamination.
- **Ethical and Bias Considerations**: Ensure fairness and minimize biases in predictions to prevent disproportionate effects on certain populations.

## Acknowledgments/References

- [Kaggle](https://www.kaggle.com)
- 365 Data Science
- Towards Data Science
- Analytics Vidhya
- Water Education
- NCBI
- Discover Data Science


