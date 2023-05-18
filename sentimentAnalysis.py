import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import statsmodels.api as sm

def sentimentAnalysis(sentiment_df):
    # print the resulting data frame
    print(sentiment_df)
    
    # Calculate the average rating
    average_rating = sentiment_df['stars'].mean()
    print('Average rating:', average_rating)

    # Calculate the total number of reviews
    total_reviews = sentiment_df['total_reviews'].sum()
    print('Total number of reviews:', total_reviews)

    # Calculate the percentage of products with a rating above the average
    above_average = sentiment_df[sentiment_df['stars'] > average_rating]
    above_average_percent = (len(above_average) / len(sentiment_df)) * 100
    print('Percentage of products with a rating above the average:', above_average_percent)

    ##PLOTS AND FIGURES## EXPLORATORY DATA ANALYSIS
    #Histogram of Ratings#
    plt.hist(sentiment_df['stars'], bins=5, range=(1,5), rwidth=0.8)
    plt.xlabel('Rating')
    plt.ylabel('Count')
    plt.title('Distribution of Ratings')
    plt.show()

    #Scatter Plot of Price vs. Ratings#
    plt.scatter(sentiment_df['price'], sentiment_df['stars'])
    plt.axhline(average_rating, color='red', linestyle='--', linewidth=2, label='Average Rating')   #adding a horizontal line at the average point
    plt.legend() 
    plt.xlabel('Price')
    plt.ylabel('Rating')
    plt.title('Price vs. Ratings')
    plt.show()

    #Bar Plot of Total Reviews by Rating#
    sns.barplot(x='stars', y='total_reviews', data=sentiment_df, palette='Blues_d')
    plt.xlabel('Rating')
    plt.ylabel('Total Reviews')
    plt.title('Total Reviews by Rating')
    plt.show()

    ##SENTIMENT ANALYSIS## SENTIMENT SCORE AND SENTIMENT GENERATION 
    # define the bin edges and labels for rating
    bin_edges = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
    bin_labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # assign rating to each value based on the bin edges and labels
    sentiment_df['star_rating'] = pd.cut(sentiment_df['stars'], bins=bin_edges, labels=bin_labels)
    sentiment_df['star_rating'] = sentiment_df['star_rating'].astype(int)

    # Calculate the maximum value of total_reviews
    max_reviews = sentiment_df['total_reviews'].max()
    # Scale the total_reviews to a range of 1 to 10
    sentiment_df['review_rating'] = sentiment_df['total_reviews'] / max_reviews * 9 + 1
    # Convert 'review_rating' column to float
    sentiment_df['review_rating'] = sentiment_df['review_rating'].astype(int)

    # Calculate the maximum value of total_reviews
    max_reviews = sentiment_df['price'].max()
    # Scale the total_reviews to a range of 1 to 10
    sentiment_df['price_rating'] = sentiment_df['price'] / max_reviews * 9 + 1
    # Round the review_rating to integer values
    sentiment_df['price_rating'] = sentiment_df['price_rating'].astype(int)

    # add a new column with rating based on value
    sentiment_df['is_best_seller_rating'] = np.where(sentiment_df['is_best_seller'], 10, 0)
    sentiment_df['is_best_seller_rating'] = sentiment_df['is_best_seller_rating'].astype(int)

    sentiment_df['sentiment_score'] = sentiment_df['star_rating']*0.3 + sentiment_df['review_rating']*0.3 + sentiment_df['price_rating']*0.2 + sentiment_df['is_best_seller_rating']*0.2

    # define the bin edges and labels for rating
    bin_edges_sentiment = [0.0, 3.0, 6.0, 10.0]
    bin_labels_sentiment = ["Negative", "Neutral", "Positive"]
    # assign rating to each value based on the bin edges and labels
    sentiment_df['sentiment'] = pd.cut(sentiment_df['sentiment_score'], bins=bin_edges_sentiment, labels=bin_labels_sentiment)
    print(sentiment_df)

    ##SENTIMENT VISUALIZATION##
    # Visualize sentiment_score using a bar plot
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(sentiment_df['sentiment_score'])), sentiment_df['sentiment_score'])
    plt.xlabel('Product')
    plt.ylabel('Sentiment Score')
    plt.title('Sentiment Score for Each Product')
    plt.xticks(range(len(sentiment_df['sentiment_score'])), range(1, len(sentiment_df['sentiment_score']) + 1))
    plt.show()

    sentiment_counts = sentiment_df['sentiment'].value_counts()
    plt.figure(figsize=(8, 6))
    plt.bar(sentiment_counts.index, sentiment_counts.values)
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.title('Distribution of Sentiment')
    plt.show()

    ##SENTIMENT SCORE VS DIFFERENT FACTORS##
    average_sentiment = sentiment_df['sentiment_score'].mean()
    # Sentiment Score vs Stars (Scatter Plot)
    plt.figure(figsize=(8, 6))
    plt.scatter(sentiment_df['stars'], sentiment_df['sentiment_score'])
    plt.axhline(average_sentiment, color='red', linestyle='--', linewidth=2, label='Average Rating')
    plt.legend()
    plt.xlabel('Stars')
    plt.ylabel('Sentiment Score')
    plt.title('Sentiment Score vs Stars')
    plt.show()

    # Sentiment Score vs Total Reviews (Scatter Plot)
    plt.figure(figsize=(8, 6))
    plt.scatter(sentiment_df['total_reviews'], sentiment_df['sentiment_score'])
    plt.axhline(average_sentiment, color='red', linestyle='--', linewidth=2, label='Average Rating')
    plt.legend()
    plt.xlabel('Total Reviews')
    plt.ylabel('Sentiment Score')
    plt.title('Sentiment Score vs Total Reviews')
    plt.show()

    # Sentiment Score vs Price Rating (Box Plot)
    plt.figure(figsize=(8, 6))
    plt.scatter(sentiment_df['price'], sentiment_df['sentiment_score'])
    plt.axhline(average_sentiment, color='red', linestyle='--', linewidth=2, label='Average Rating')
    plt.legend()
    plt.xlabel('Price')
    plt.ylabel('Sentiment Score')
    plt.title('Sentiment Score vs Price')
    plt.show()

def mostImportantFactor(sentiment_df):
    # Convert columns to numeric types
    sentiment_df['stars'] = pd.to_numeric(sentiment_df['stars'], errors='coerce')
    sentiment_df['price'] = pd.to_numeric(sentiment_df['price'], errors='coerce')
    sentiment_df['total_reviews'] = pd.to_numeric(sentiment_df['total_reviews'], errors='coerce')

    # Drop rows with missing values
    sentiment_df = sentiment_df.dropna(subset=['stars', 'price', 'total_reviews'])

    # Prepare the data
    X = sentiment_df[['stars', 'price', 'total_reviews']]
    X = sm.add_constant(X)  # Add a constant term for the intercept
    y = sentiment_df['is_best_seller'].astype(bool)  # Convert to boolean type

    # Fit the logistic regression model
    model = sm.Logit(y, X)
    results = model.fit()

    # Get the model summary
    print(results.summary())

    # Predict the most important factor
    coefficients = results.params[1:]
    most_important_factor = coefficients.idxmax()
    print("The most important factor is:", most_important_factor)