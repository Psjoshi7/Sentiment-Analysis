import pandas as pd

# create an empty data frame with custom column names
sentiment_df = pd.DataFrame(columns=['name', 'stars', 'total_reviews', 'price', 'is_best_seller'])
def dataExtraction(more_data):
# iterate through the list of dictionaries in more_data
    for item in more_data:
        # extract relevant information from the dictionary
        name = item['name']
        if 'stars' in item and item['stars'] is not None:
            stars = float(item['stars']) if isinstance(item['stars'], str) else item['stars']
        else:
            stars = 0.0  # Replace NA or null with 0.0 for float column
        if 'total_reviews' in item and item['total_reviews'] is not None:
            total_reviews = int(item['total_reviews']) if isinstance(item['total_reviews'], str) else item['total_reviews']
        else:
            total_reviews = 0  # Replace NA or null with 0 for integer column
        if 'price' in item and item['price'] is not None:
            price = float(item['price'].replace('$','').replace(',','')) if isinstance(item['price'], str) else item['price']
        else:
            price = 0.0  # Replace NA or null with 0.0 for float column
        if 'is_best_seller' in item:
            is_best_seller = item['is_best_seller']
        else:
            is_best_seller = False  # Replace NA or null with False for boolean column
        
        # append the information as a new row to the data frame
        global sentiment_df
        sentiment_df = sentiment_df.append({'name': name, 'stars': stars, 'total_reviews': total_reviews, 'price': price, 'is_best_seller':is_best_seller}, ignore_index=True)
    return sentiment_df
    
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
    return sentiment_df

def dataExtraction3(more_data):
# iterate through the list of dictionaries in more_data
    for item in more_data:
        # extract relevant information from the dictionary
        name = item['title']
        stars = float(item['reviews']['rating']) if isinstance(item['reviews']['rating'], str) else item['reviews']['rating']
        if 'reviews' in item and 'rating' in item['reviews']:
            stars = float(item['reviews']['rating']) if isinstance(item['reviews']['rating'], str) else item['reviews']['rating']
        else:
            stars = 0.0  # Replace NA or null with 0.0 for float column
        total_reviews = item['reviews']['total_reviews']
        if 'reviews' in item and 'total_reviews' in item['reviews']:
            total_reviews = int(item['reviews']['total_reviews']) if isinstance(item['reviews']['total_reviews'], str) else item['reviews']['total_reviews']
        else:
            total_reviews = 0  # Replace NA or null with 0 for integer column
        if 'price' in item and 'current_price' in item['price']:
            price = float(item['price']['current_price'].replace('$','').replace(',','')) if isinstance(item['price']['current_price'], str) else item['price']['current_price']
        else:
            price = 0.0  # Replace NA or null with 0.0 for float column
        if 'bestSeller' in item:
            is_best_seller = item['bestSeller']
        else:
            is_best_seller = False  # Replace NA or null with False for boolean column
        
        # append the information as a new row to the data frame
        global sentiment_df
        sentiment_df = sentiment_df.append({'name': name, 'stars': stars, 'total_reviews': total_reviews, 'price': price, 'is_best_seller':is_best_seller}, ignore_index=True)
    return sentiment_df