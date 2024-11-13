# TweetSentiment Social Media Insights

## Project Overview
Using Natural Language Processing (NLP), this project performs sentiment analysis on tweets to determine whether they express positive, negative, or neutral sentiments. By leveraging machine learning, it helps brands and organizations understand public opinion, monitor trends, and gauge customer feedback on social media platforms.

## Table of Contents
1. Project Overview
2. Installation and Setup
3. Python Packages Used
4. Data
5. Source Data
6. Results and Evaluation
7. Future Work
8. Acknowledgments/References

## Installation and Setup
1. **Install Anaconda**: Download and install Anaconda from [Anaconda's official website](https://www.anaconda.com/products/distribution).
2. **Open Anaconda Navigator**: Launch Anaconda Navigator from your application menu or command line.
3. **Open Jupyter Notebook**: Click on the Jupyter Notebook icon in Anaconda Navigator to open it in your web browser.
4. **Create or Open a Notebook**: Create a new notebook or open an existing one to start working with Python.

## Python Packages Used
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- nltk
- tweepy
- textblob
- vaderSentiment

## Data
The dataset used for this term project can be accessed on Kaggle and includes 74,682 records for training and 1,000 records for validation. Each record represents a tweet categorized into different sentiment classes. The dataset comprises the following key variables:

- **Tweet_ID**: A unique identifier for each tweet.
- **Entity**: The source or context of the tweet, such as a game or brand name.
- **Sentiment**: The sentiment classification of the tweet (e.g., Positive, Negative, Neutral, or Irrelevant).
- **Tweet_content**: The actual text of the tweet, which serves as the primary input for sentiment analysis.

This dataset includes labeled tweets that will be used for training and validating sentiment analysis models.

### Source Data
The dataset used in this project was sourced from Kaggle's Twitter Sentiment Dataset. Ensure you download the dataset and place it in the appropriate directory within the project folder.

## Results and Evaluation
The comprehensive evaluation confirmed that the models performed reliably, achieving strong results across all key metrics. This demonstrates their effectiveness in classification tasks and supports their deployment in real-world applications. Continued refinement and enhancement of the models could lead to even better performance, addressing any potential limitations identified during the evaluation.

### Key Findings:
The LinearSVC model was the most effective for sentiment analysis, showing high accuracy and performance after hyperparameter tuning. It successfully addressed class imbalance and sentiment differentiation. Future work should refine the model further and explore advanced techniques to improve accuracy and handle language diversity.

### Model Performance:
The LinearSVC model performed best with an accuracy of 89%, excelling across all sentiment categories. Multinomial Naive Bayes and Logistic Regression also showed strong results, while Bernoulli Naive Bayes performed well in specific areas but had room for improvement.

## Future Work
Future work will include integrating advanced models like LSTM and BERT to better handle sarcasm and emojis, expanding the dataset for improved accuracy, and developing scalable infrastructure for real-time sentiment analysis.

## Acknowledgments/References
- [Kaggle](https://www.kaggle.com/)
- 365 Data Science
- Towards Data Science
- Analytics Vidhya
- [Techsalerator](https://www.techsalerator.com/post/top-x-twitter-sentiment-data-providers)
- [Medium - X (Twitter) Sentiment Analysis](https://medium.com/@ubaidhaina/x-twitter-sentiment-analysis-05decd00a29f)
- [ResearchGate - X (Twitter) Sentiment Analysis](https://www.researchgate.net/publication/358439871_X_Twitter_Sentiment_Analysis_using_Natural_Language_Processing)
- [Twitter](https://twitter.com/)
