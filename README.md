[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/6ebMFVGY)
# IE 555 Project Proposal Template

---

## Team Members:  
- **Prajakta Joshi**, **pjoshi7@buffalo.edu** 
- **Yateen Natekar**, **yateensa@buffalo.edu**
- **Amey Ekkaldevi**, **ameybalr@buffalo.edu**
- **Dhiraj Bhandari**, **dhirajpa@buffalo.edu**

---

## Proposed Project Title

- **Sentimental Analysis of Customer Based Reviews**

--- 
 
### Option 2 - Online Data Analysis

#### Data Sources
- We will be utilizing the Rapid API data source to fetch Amazon product information. This data set includes the following information
- Best sellers , reviews, rating stars, manufacturers, Product names, prices, etc
- Using these attributes we will be performing sentimental analysis for different products across the ecommerce platform.
    - Links

#### Analysis Plan
- *_Analysis:
    Performing sentimenatl analysis for diferent products will involve the following analyses with the data:_*

- *_Product performance analysis:
This analysis will help in identifying the most and least selling products, the products with popularity status, and their impact on the overall rating performance of the company. The following data fields will be required for this analysis:_*

    Product names, Categories, Descriptions, Cost price, ratings, reviews

- *_To conduct this analysis, we can use Python's Pandas library to extract the required data from the ecommerce platform database. We can then calculate the criteria weightage and rank them based on their performance. This analysis can help in identifying the products that are driving the company's popularity and those that are not performing well. The analysis can also help in making informed decisions about pricing, promotions, and product development._*

- *_Sentiment Analysis:_*
- *_This analysis will help in interpreting the product sentiments, product perfomrance referring reviews and indentifying the best selling products. The following data fields will be required for this analysis:_*
 
   Product names, Descriptions, Ratings, reviews, Cost, Best seller factor 
 
 - *_To conduct analysis, we can use Python's pandas library to extract the data various API keys. We can then calculate the weightage for 4 parameters of various products. This analysis can apply a sentiment analysis model to determine the sentiment polarity (positive, negative, or neutral) of each customer review and associate the sentiment with the corresponding rating and price of each product. The analysis can also help in exploring the distribution of sentiment scores across the dataset and in Calculating individual sentiment scores for different rating levels (e.g., 1-2 stars, 3-4 stars, 5 stars) to identify any patterns or trends._*


- *_colleration analysis:
This analysis will help in understanding customer sentiments can give businesses a strategic advantage and the relationship between ratings, reviews, and prices to uncover patterns or associations. The following data fields will be required for this analysis:_*

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
| 2 | Project planning and preparation | 2023-04-20 | DONE |
| 3 | Research and selection of appropriate API data sources (Inventory review data using Rapid API) | 2023-04-25 | DONE |
| 4 | Setting up API authentication and gathering product review data from different API/platforms| 2023-04-28 | DONE |
| 5a | Data Preprocessing and combining data from different API/platform | 2023-05-01 | Done |
| 5b | Data Cleaning and Selection of defined product attributes | 2023-05-03 | Done |
| 6a | Exploratory sentiment data analysis and visualization | 2023-05-09 | In Progress |
| 6b | Comparitive analysis between different product categories and platforms | 2023-05-12 | In Progress |
| 7 | Sentiment Analysis Interpretation | 2023-05-14 | Yet to Start |
| 8 | Concluding the Analysis and creating Final Report | 2023-05-15 | Yet to Start |
| 9 | Complete YouTube video and upload to YouTube | 2023-05-16 | Yet to Start |
| 10 | Upload README.md document to Github | 2023-05-17 | Yet to Start |

--- 

## Introduction
The purpose of this section is to provide some background about your project.  For example, your introduction should discuss
- The purpose of your project;
- The type of data you're using;
- What you're doing with this data;
- What types of analysis you're conducting;

Your introduction should make the reader excited to read the rest of this document.

- Introduction:

In today's digital age, electronic products have become an integral part of our lives. Whether it's smartphones, laptops, or home appliances, consumers rely heavily on online platforms to make informed purchasing decisions. With the abundance of choices available, customers often turn to customer reviews, star ratings, and prices to gauge the quality and suitability of electronics products.

The purpose of this project is to delve into the world of sentiment analysis and leverage the power of data to gain valuable insights into customer sentiments towards electronics products. By analyzing customer reviews, star ratings, and prices, we aim to extract meaningful information that can aid both consumers and manufacturers in making informed decisions.

The data used for this project consists of a vast collection of customer reviews, star ratings, and corresponding prices of various electronics products from popular online platforms. Each review provides a unique perspective on the strengths, weaknesses, and overall satisfaction of customers with a particular product.

With this data, we are embarking on a comprehensive analysis to understand the sentiment behind these customer reviews. Our goal is to develop a sentiment analysis model that can automatically classify reviews as positive, negative, or neutral based on the expressed opinions. By employing natural language processing techniques, we will extract important features and sentiments from textual data, and combine them with star ratings and prices to gain deeper insights into the customer's overall experience.

Throughout this project, we will conduct various analyses to uncover patterns, trends, and correlations within the dataset. We will explore the relationship between customer sentiments, star ratings, and prices to identify factors that contribute to positive or negative feedback. Additionally, we will investigate the impact of different product categories, brands, and price ranges on customer satisfaction.

By the end of this project, we aim to present a comprehensive analysis report that not only reveals the sentiment trends in electronics products but also provides actionable insights for manufacturers to improve their products and for consumers to make more informed decisions.

Join us on this exciting journey as we dive into the realm of sentiment analysis, uncovering the hidden stories within customer reviews, star ratings, and prices of electronics products. Get ready to explore the world of data-driven decision-making, where sentiments meet technology, and where knowledge transforms into power.

---

## References
In this section, provide links to your references and data sources.  For example:
- Source code was adapted from [the magic source code farm](http://www.amagicalnonexistentplace.com)
- The code retrieves data from [the organization for hosting cool data](http://www.anothermagicalnonexistentplace.com)
- The forecasting models were modified from [some academic research paper](http://www.linktotheacademicpaperyouused.com)

---


