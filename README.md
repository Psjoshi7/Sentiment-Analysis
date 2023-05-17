[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/6ebMFVGY)


---

## Team Members:  
- **Prajakta Joshi**, **pjoshi7@buffalo.edu** 
- **Yateen Natekar**, **yateensa@buffalo.edu**
- **Amey Ekkaldevi**, **ameybalr@buffalo.edu**
- **Dhiraj Bhandari**, **dhirajpa@buffalo.edu**

---

## Project Title

- **Sentiment Analysis of Consumer Based Electronic Product Reviews**
--- 
 
### Option 2 - Online Data Analysis

#### Data Sources
- We will be utilizing the Rapid API data source to fetch Amazon product information. This data set includes the following information
- Best sellers , reviews, rating stars, manufacturers, Product names, prices, etc
- Using these attributes we will be performing sentiment analysis for different products across the ecommerce platform Amazon.

#### Analysis Plan
 *_Analysis:
    Performing sentimenatl analysis for diferent products will involve the following analyses with the data:_*

- *_Product performance analysis:
This analysis will help in identifying the most and least selling products, the products with popularity status, and their impact on the overall rating performance of the company. The following data fields will be required for this analysis:_*

    Product names, Categories, Descriptions, Cost price, ratings, reviews

- *_To conduct this analysis, we can use Python's Pandas library to extract the required data from the ecommerce platform database. We can then calculate the criteria weightage and rank them based on their performance. This analysis can help in identifying the products that are driving the company's popularity and those that are not performing well. The analysis can also help in making informed decisions about pricing, promotions, and product development._*

 **_Sentiment Analysis:_**
- *_This analysis will help in interpreting the product sentiments, product perfomrance referring reviews and indentifying the best selling products. The following data fields will be required for this analysis:_*
 
   Product names, Descriptions, Ratings, reviews, Cost, Best seller factor 
 
 - *_To conduct analysis, we can use Python's pandas library to extract the data various API keys. We can then calculate the weightage for 4 parameters of various products. This analysis can apply a sentiment analysis model to determine the sentiment polarity (positive, negative, or neutral) of each customer review and associate the sentiment with the corresponding rating and price of each product. The analysis can also help in exploring the distribution of sentiment scores across the dataset and in Calculating individual sentiment scores for different rating levels (e.g., 1-2 stars, 3-4 stars, 5 stars) to identify any patterns or trends._*


**_colleration analysis:_**
This analysis will help in understanding customer sentiments can give businesses a strategic advantage and the relationship between ratings, reviews, and prices to uncover patterns or associations. The following data fields will be required for this analysis:
  
    Best seller factor, price, ratings

- *_To conduct this analysis, we can use python's pandas library to generate regression analysis. We can determine if there is a correlation between price and customer satisfaction, or if high ratings are associated with higher prices. Correlation analysis can provide insights into the factors that influence customer perceptions and purchasing decisions.This analysis can analyze the correlation coefficients and their statistical significance to draw conclusions._*

#### Motivation
- *_Understanding Consumer Sentiments: In today's digital era, online reviews play a significant role in influencing consumer decisions. By analyzing customer reviews, star ratings, and prices of electronics products, we can gain valuable insights into consumer sentiments. This project aims to leverage the power of sentiment analysis to understand how customers perceive and evaluate various electronics products.
    Enhancing Product Development: Sentiment analysis can provide crucial feedback for product development teams. By analyzing customer reviews, companies can identify strengths and weaknesses of their products. This information can be used to make informed decisions about product improvements, feature enhancements, or even the development of new products that align with customer preferences and expectations.
    Pricing Strategies: The sentiment analysis of customer reviews can also be used to optimize pricing strategies. By correlating sentiment scores with product prices, companies can identify the optimal price range that aligns with positive customer sentiments. This information can guide businesses in setting competitive prices while maximizing their profitability.
    Customer Satisfaction and Retention: Positive customer sentiment is directly linked to customer satisfaction and retention. By identifying factors that contribute to positive sentiments, businesses can enhance customer experiences and build stronger relationships with their customers. This project can help identify specific features, qualities, or aspects of electronics products that drive positive sentiments, enabling businesses to focus their efforts on delivering what customers value the most.
    Academic Research and Innovation: This project can serve as a foundation for academic research and innovation in the field of sentiment analysis. Researchers and students can explore and improve upon existing techniques, algorithms, and models in the context of electronics product reviews. The findings and methodologies developed through this project can contribute to the advancement of sentiment analysis and its applications in various domains._*

---
## Task List

| ID | Task Description | Due Date | Status |
| --- | --- | --- | --- |
| 1 | Project Proposal | 2023-04-18 | Done |
| 2 | Project planning and preparation | 2023-04-20 | Done |
| 3 | Research and selection of appropriate API data sources (Inventory review data using Rapid API) | 2023-04-25 | Done |
| 4 | Setting up API authentication and gathering product review data from different API/platforms| 2023-04-28 | Done |
| 5a | Data Preprocessing and combining data from different API/platform | 2023-05-01 | Done |
| 5b | Data Cleaning and Selection of defined product attributes | 2023-05-03 | Done |
| 6 | Exploratory sentiment data analysis and visualization | 2023-05-09 | Done |
| 7 | Sentiment Analysis Interpretation | 2023-05-14 | Done |
| 8 | Concluding the Analysis and creating Final Report | 2023-05-15 | Done |
| 9 | Complete YouTube video and upload to YouTube | 2023-05-16 | Done |
| 10 | Upload README.md document to Github | 2023-05-17 | In Progress |
| 11 | Comparitive analysis between different product categories and platforms | - | Future Scope |

--- 

## Introduction

- In today's digital age, electronic products have become an integral part of our lives. Whether it's smartphones, laptops, or home appliances, consumers rely heavily on online platforms to make informed purchasing decisions. With the abundance of choices available, customers often turn to customer reviews, star ratings, and prices to gauge the quality and suitability of electronics products.

- The purpose of this project is to delve into the world of sentiment analysis and leverage the power of data to gain valuable insights into customer sentiments towards electronics products. By analyzing customer reviews, star ratings, and prices, we aim to extract meaningful information that can aid both consumers and manufacturers in making informed decisions.

- The data used for this project consists of a vast collection of customer reviews, star ratings, and corresponding prices of various electronics products from popular online platforms. Each review provides a unique perspective on the strengths, weaknesses, and overall satisfaction of customers with a particular product.

- With this data, we are embarking on a comprehensive analysis to understand the sentiment behind these customer reviews. Our goal is to develop a sentiment analysis model that can automatically classify reviews as positive, negative, or neutral based on the expressed opinions. By employing natural language processing techniques, we will extract important features and sentiments from textual data, and combine them with star ratings and prices to gain deeper insights into the customer's overall experience.

- Throughout this project, we will conduct various analyses to uncover patterns, trends, and correlations within the dataset. We will explore the relationship between customer sentiments, star ratings, and prices to identify factors that contribute to positive or negative feedback. Additionally, we will investigate the impact of different product categories, brands, and price ranges on customer satisfaction.

- By the end of this project, we aim to present a comprehensive analysis report that not only reveals the sentiment trends in electronics products but also provides actionable insights for manufacturers to improve their products and for consumers to make more informed decisions.

- Join us on this exciting journey as we dive into the realm of sentiment analysis, uncovering the hidden stories within customer reviews, star ratings, and prices of electronics products. Get ready to explore the world of data-driven decision-making, where sentiments meet technology, and where knowledge transforms into power.

---

## References
In this section, provide links to your references and data sources.  
1. Rapid API website links for:
 - for Iphone : https://rapidapi.com/letscrape-6bRBa3QguO5/api/real-time-amazon-data/
	- for Gaming Headset : https://rapidapi.com/dsmlhidroponia/api/amazon-scraper-sm/
	- for Mackbook : https://rapidapi.com/a19476210/api/h-amazon-data-scraper2/
	- for Xbox : https://rapidapi.com/restyler/api/amazon23
2. Chat GPT prompts:
---

## Requirements
- ### Dependencies

The following packages are required to run the project:

- pandas
- requests
- tkinter
- ### Installation

To install the project dependencies, use the following command:

```bash
pip install pandas 
pip install requests 
pip install tkinter
```
# Explanation of the Code

The code, `PJOSHI7_IE555_Project.py`, begins by importing necessary Python packages:
The below code is the Python script that enables users to select an option from a dropdown menu in a pop-up window. It uses the tkinter library for creating the graphical user interface (GUI). 
```
import pandas as pd
import requests
import tkinter as tk
from tkinter import ttk
import dataExtraction as de
import sentimentAnalysis as sa

# Create a function to capture the user input
def submit():
    print("You selected: ", selected_option.get())
    window.destroy()

# Create a pop-up window
window = tk.Tk()
window.geometry("600x300") # set the dimensions of the window
window.title("Electronics Product Sentiment Analysis")

# Create a message label
message_label = tk.Label(window, text="Please select an option for which you want to see the sentiment analysis:", font=("Arial", 12))
message_label.pack(pady=10)

# Create a dropdown menu with some options
options = ["Select", "Iphone", "Xbox", "Gaming Headset", "MacBook"]
selected_option = tk.StringVar(window)
selected_option.set(options[0]) # set the default value
dropdown = ttk.OptionMenu(window, selected_option, *options)
dropdown.pack(pady=10)
# Create a submit button
submit_button = tk.Button(window, text="Submit", font=("Arial", 12), command=submit)
submit_button.pack(pady=10)

# Start the main event loop
window.mainloop()
product = selected_option.get()
```

The script imports the necessary libraries: pandas, requests, and tkinter.
It also imports two custom modules: dataExtraction and sentimentAnalysis, which are likely used for data processing and analysis.
The submit() function is defined to handle the user's selection from the dropdown menu. It prints the selected option and closes the window.
A pop-up window is created using tkinter.Tk() and configured with a specific size and title.
A label is added to display a message to the user.
A dropdown menu is created using the ttk.OptionMenu widget, allowing the user to select an option from the provided list.
A submit button is added to trigger the submit() function when clicked.
The main event loop, window.mainloop(), starts to handle user interactions and display the GUI.
The selected option from the dropdown menu is stored in the product variable for further processing or analysis.

---
## API Connection generation
This script performs sentiment analysis on Amazon product data, specifically for the "Iphone" category. It extracts data from the Real-Time Amazon API, analyzes the sentiment of the extracted data, and identifies the most important factors affecting the sentiment.

``` 
##Real-Time Amazon Data##
elif (product == "Iphone"):

    url = "https://real-time-amazon-data.p.rapidapi.com/search"

    querystring = {"query":"iPhone","page":"1","country":"US","category_id":"aps"}

    headers = {
        "X-RapidAPI-Key": "d64344274emsh6073228e1bc2f43p165551jsn9753ae716a86",
        "X-RapidAPI-Host": "real-time-amazon-data.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    more_data = data['data']['products']
    type(more_data)
    sentiment_df = de.dataExtraction2(more_data)
    print("Data Extraction Done")
    sa.sentimentAnalysis(sentiment_df)
    print("Sentiment Analysis Done")
    sa.mostImportantFactor(sentiment_df)
    print("Regression Done")
	
```
The above code is a conditional block that executes when the selected product is "Iphone". It specifies the URL, query parameters, and headers required to make an API request .
The requests.get() function is used to send an HTTP GET request to the specified URL, including the necessary headers and query parameters.
The response from the API request is stored in the response variable.
The response data is retrieved in JSON format using response.json(), and the relevant data is extracted and assigned to the more_data variable.
The extracted data is then passed to the dataExtraction() function from the dataExtraction module for further processing.
The dataExtraction() function likely performs data extraction and transformation tasks specific to the "Iphone" data.
After data extraction, the sentimentAnalysis() function from the sentimentAnalysis module is called to perform sentiment analysis on the extracted data.
Finally, the mostImportantFactor() function from the sentimentAnalysis module is called to determine the most important factor influencing sentiment.
The results of each step are printed to the console.

---
## Data Extraction
```
import pandas as pd

# create an empty data frame with custom column names
sentiment_df = pd.DataFrame(columns=['name', 'stars', 'total_reviews', 'price', 'is_best_seller'])
def dataExtraction2(more_data):
# iterate through the list of dictionaries in more_data
    for item in more_data:
        # extract relevant information from the dictionary
        name = item['product_title']
        if 'product_star_rating' in item and item['product_star_rating'] is not None:
            stars = float(item['product_star_rating']) if isinstance(item['product_star_rating'], str) else item['product_star_rating']
        else:
            stars = 0.0  # Replace NA or null with 0.0 for float column
        if 'product_num_ratings' in item and item['product_num_ratings'] is not None:
            total_reviews = int(item['product_num_ratings']) if isinstance(item['product_num_ratings'], str) else item['product_num_ratings']
        else:
            total_reviews = 0  # Replace NA or null with 0 for integer column
		if 'product_price' in item and item['product_price'] is not None:
            price = float(item['product_price'].replace('$','').replace(',','')) if isinstance(item['product_price'], str) else item['product_price']
        else:
            price = 0.0  # Replace NA or null with 0.0 for float column
        if 'is_best_seller' in item:
            is_best_seller = item['is_best_seller']
        else:
            is_best_seller = False  # Replace NA or null with False for boolean column
        
        # append the information as a new row to the data frame
        global sentiment_df
        sentiment_df = sentiment_df.append({'name': name, 'stars': stars, 'total_reviews': total_reviews, 'price': price, 'is_best_seller':is_best_seller}, ignore_index=True)
    return sentiment_df
```
The provided code defines a function named dataExtraction that performs data extraction from a list of dictionaries (more_data) obtained from an API. The extracted data is then stored in a Pandas DataFrame named sentiment_df. 
The function takes the more_data list as input.
It iterates through each dictionary in the more_data list.
Inside the loop, relevant information such as name, stars, total_reviews, price, and is_best_seller is extracted from each dictionary.
The extracted values are checked for null or None values, and if necessary, they are replaced with appropriate default values (0.0, 0, or False).
The extracted information is appended as a new row to the sentiment_df DataFrame using the DataFrame.append() method.
Finally, the function returns the updated sentiment_df DataFrame.
This function is called within the PJOSHI7_IE555_Project.py file to extract data from the API response and populate the sentiment_df DataFrame with the extracted information.

---
## Data Exploratory Analysis 
```
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
```
 The provided code defines a function named sentimentAnalysis that performs initial analysis and generates exploratory plots for the sentiment_df DataFrame.
The function takes the sentiment_df DataFrame as input.
It starts by printing the content of the DataFrame using print(sentiment_df).
It calculates the average rating by taking the mean of the 'stars' column and prints it.
It calculates the total number of reviews by summing the 'total_reviews' column and prints it.
It identifies the percentage of products with a rating above the average rating and prints it.
The function then proceeds to create exploratory plots using Matplotlib and Seaborn:
It creates a histogram of ratings using plt.hist() function to visualize the distribution of ratings.
It creates a scatter plot of price versus ratings using plt.scatter() function to explore the relationship between price and ratings.
It creates a bar plot of total reviews by rating using sns.barplot() function to analyze the distribution of total reviews across different ratings.
Each plot is customized with appropriate labels and titles.
Finally, the plots are displayed using plt.show().
This function is called within the PJOSHI7_IE555_Project.py file to perform initial analysis and generate exploratory plots based on the data in the sentiment_df DataFrame.

---
## Sentiment Analysis
```
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
```
The provided code calculates a sentiment score and assigns a sentiment value to each row in the sentiment_df DataFrame based on several columns. Here's a brief explanation of the code:

The code defines two lists: bin_edges and bin_labels, which represent the bin edges and labels for rating.
The 'stars' column in sentiment_df is transformed into discrete ratings using pd.cut() with the specified bin edges and labels. The resulting ratings are stored in a new column named 'star_rating'.
The 'total_reviews' column is scaled to a range of 1 to 10 based on the maximum value in the column. The scaled values are stored in a new column named 'review_rating'.
The 'price' column is also scaled to a range of 1 to 10 based on the maximum value in the column. The scaled values are stored in a new column named 'price_rating'.
A new column named 'is_best_seller_rating' is added, which has a value of 10 if the corresponding row in the 'is_best_seller' column is True, and 0 otherwise.
The sentiment score is calculated by combining the ratings from 'star_rating', 'review_rating', 'price_rating', and 'is_best_seller_rating' columns, using appropriate weights (0.3, 0.3, 0.2, and 0.2, respectively). The resulting scores are stored in a new column named 'sentiment_score'.
Another set of bin edges and labels is defined for sentiment based on the sentiment score.
The 'sentiment_score' column is transformed into discrete sentiment values using pd.cut() with the specified bin edges and labels. The resulting sentiment values are stored in a new column named 'sentiment'.
Finally, the updated DataFrame with the added columns is printed using print(sentiment_df).
The sentiment score is generated by combining the ratings from different columns (stars, total_reviews, price, is_best_seller) with specific weights assigned to each column. These weights determine the relative importance of each factor in determining the sentiment score. The sentiment score is then categorized into sentiment values (Negative, Neutral, Positive) based on predefined bin edges and labels. This process allows for a quantification of sentiment based on the provided data.

---
## Sentiment Visualisation
```
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
    # Sentiment Score vs Stars (Scatter Plot)
    plt.figure(figsize=(8, 6))
    plt.scatter(sentiment_df['stars'], sentiment_df['sentiment_score'])
    plt.xlabel('Stars')
    plt.ylabel('Sentiment Score')
    plt.title('Sentiment Score vs Stars')
    plt.show()

	# Sentiment Score vs Total Reviews (Scatter Plot)
    plt.figure(figsize=(8, 6))
    plt.scatter(sentiment_df['total_reviews'], sentiment_df['sentiment_score'])
    plt.xlabel('Total Reviews')
    plt.ylabel('Sentiment Score')
    plt.title('Sentiment Score vs Total Reviews')
    plt.show()

    # Sentiment Score vs Price Rating (Box Plot)
    plt.figure(figsize=(8, 6))
    plt.scatter(sentiment_df['price'], sentiment_df['sentiment_score'])
    plt.xlabel('Price')
    plt.ylabel('Sentiment Score')
    plt.title('Sentiment Score vs Price')
    plt.show()
```
The provided code includes several visualizations to analyze sentiment scores and their relationship with different factors. Here's a brief explanation of each plot:

Bar Plot of Sentiment Scores: This plot visualizes the sentiment scores for each product using a bar plot. Each product is represented on the x-axis, and the corresponding sentiment score is shown on the y-axis. The height of each bar represents the sentiment score of the product.

Distribution of Sentiment: This plot displays the distribution of sentiment values across all products. It uses a bar plot where the x-axis represents the sentiment categories (Negative, Neutral, Positive), and the y-axis represents the count of products in each sentiment category.

Sentiment Score vs Stars (Scatter Plot): This scatter plot shows the relationship between the sentiment scores and the stars (ratings) of the products. Each point represents a product, and the x-axis represents the stars (ratings), while the y-axis represents the sentiment scores. The scatter plot helps visualize any patterns or trends between stars and sentiment scores.

Sentiment Score vs Total Reviews (Scatter Plot): This scatter plot explores the relationship between the sentiment scores and the total number of reviews for the products. The x-axis represents the total number of reviews, and the y-axis represents the sentiment scores. It provides insights into how sentiment scores correlate with the popularity or feedback received by the products.

Sentiment Score vs Price (Box Plot): This box plot showcases the relationship between the sentiment scores and the prices of the products. The x-axis represents the price range, and the y-axis represents the sentiment scores. The box plot provides a visual summary of the distribution of sentiment scores within different price ranges and helps identify any outliers or trends.

Each plot serves to visualize different aspects of the sentiment analysis results, allowing for a better understanding of the relationship between sentiment scores and various factors such as stars, total reviews, and price.

```
##SENTIMENT SCORE VS DIFFERENT FACTORS##
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
```
The provided code defines a function called mostImportantFactor that performs logistic regression to determine the most important factor for predicting whether a product will be a best seller. Here's a brief explanation of the code:

Data Preparation: The function starts by converting relevant columns (stars, price, total_reviews) in the sentiment_df dataframe to numeric types using pd.to_numeric. Any rows with missing values in these columns are dropped using dropna.

Model Fitting: The independent variables (stars, price, total_reviews) are assigned to X, and a constant term is added to X using sm.add_constant for the intercept. The dependent variable, is_best_seller, is converted to a boolean type and assigned to y. A logistic regression model is then fitted using sm.Logit by passing y and X as arguments.

Model Summary: The fitted model is stored in results, and the summary of the logistic regression model is printed using results.summary(). This summary provides information about the coefficients, their statistical significance, and other relevant statistical measures.

Most Important Factor: The coefficients from the logistic regression model are retrieved using results.params[1:], excluding the intercept. The factor with the highest coefficient value is identified as the most important factor using coefficients.idxmax(). The result is printed as "The most important factor is: [factor name]".

In summary, the mostImportantFactor function performs logistic regression to analyze the importance of factors (stars, price, and total reviews) in predicting the likelihood of a product being a best seller. It provides insights into which factor has the most significant influence on the outcome.


---

## How to Run the Code
*The provided python file will run as it is without subscribing to any API as they have already been subscribed by our account. The Key and Host values will run based on the current subscription.*
1. 	To create your own API key for your analysis do the following:
	Ensure that you have registered for the API key available from the Link provided .  
	- for Iphone : https://rapidapi.com/letscrape-6bRBa3QguO5/api/real-time-amazon-data/
	- for Gaming Headset : https://rapidapi.com/dsmlhidroponia/api/amazon-scraper-sm/
	- for Mackbook : https://rapidapi.com/a19476210/api/h-amazon-data-scraper2/
	- for Xbox : https://rapidapi.com/restyler/api/amazon23
	Select the product link which you want to use for the sentiment analysis.
	Subscribe to the API by selecting the free hardlimit option for API requests. Once subscribed go to the endpoints tab and select the 'GET' function thaat contains the word 'search'. Test the endpoint to check if the endpoint succeds in retriving the data. When successful, copy the code snippet for Python-> Requests from the dropdown menu and paste inside the respective product IF block replacing the existing code with your newely generated API Key.
2. Ensure that you have installed necessary Python packages. Refer to the Requirements section and Install the mentioned packages. 
3. Open Anaconda Navigator and launch 'Visual studio'. Once open select the repository that contains all 3 files mentioned below:
	- The main file: PJOSHI7_IE555_Project.py
	- Data extraction file: dataExtraction.py
	- Sentiment analysis file: sentimentAnalysis.py
4. Run the 'PJOSHI7_IE555_Project.py' file 
5. A popup window will open that comprises of a dropdown consisting of the list of products for which sentiment analysis can be carried out. 
6. select one of the options and hit the submit button. [ here the above code is explained for profduct type = Iphone ]
7. Initial analysis of the data can be seen in the terminal window. Relevent data exploratory plots will popup on the screen. 
8. close the first graph to be able to see the next graph. 
9. Once you check all the graph the sentiment analysis data can be seen in the termminal window, followed by the sentiment analysis graphs.
10. close the first sentiment analysis graph to see the next one. 
11. Once all graphs are shown the terminal will show a summary of the logistic regression carried out on the response variable 'is_best_seller' and will show the most important factor for the product to be the best seller. 





