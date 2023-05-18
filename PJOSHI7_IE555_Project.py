#IE 555 Project
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

##Amazon-scraper-sm## 
if(product == "Gaming Headset"):

    url = "https://amazon-scraper-sm.p.rapidapi.com/search/Gaming%20Headset"

    querystring = {"api_key":"c64e091eb7a27b10d05ed6e6c29b51a8"}

    headers = {
	    "X-RapidAPI-Key": "d64344274emsh6073228e1bc2f43p165551jsn9753ae716a86",
	    "X-RapidAPI-Host": "amazon-scraper-sm.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    more_data = data['results']
    type(more_data)
    sentiment_df = de.dataExtraction(more_data)
    print("Data Extraction Done")
    sa.sentimentAnalysis(sentiment_df)
    print("Sentiment Analysis Done")
    sa.mostImportantFactor(sentiment_df)
    print("Regression Done")

##Amazon Data Scraper##
elif (product == "MacBook"):
    
    url = "https://h-amazon-data-scraper2.p.rapidapi.com/search/MacBook%20Air"

    querystring = {"api_key":"70201ee0c8ed29661bc6ae00a84341fb"}

    headers = {
        "X-RapidAPI-Key": "d64344274emsh6073228e1bc2f43p165551jsn9753ae716a86",
        "X-RapidAPI-Host": "h-amazon-data-scraper2.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    more_data = data['results']
    type(more_data)
    sentiment_df = de.dataExtraction(more_data)
    print("Data Extraction Done")
    sa.sentimentAnalysis(sentiment_df)
    print("Sentiment Analysis Done")
    sa.mostImportantFactor(sentiment_df)
    print("Regression Done")

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

##Amazon##
elif(product == "Xbox"):
    url = "https://amazon23.p.rapidapi.com/product-search"

    querystring = {"query":"xbox","country":"US"}

    headers = {
        "X-RapidAPI-Key": "d64344274emsh6073228e1bc2f43p165551jsn9753ae716a86",
        "X-RapidAPI-Host": "amazon23.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    more_data = data['result']
    type(more_data)
    sentiment_df = de.dataExtraction3(more_data)
    print("Data Extraction Done")
    sa.sentimentAnalysis(sentiment_df)
    print("Sentiment Analysis Done")
    #sa.mostImportantFactor(sentiment_df)
    #print("Regression Done")
else:
    print("No API developed yet")