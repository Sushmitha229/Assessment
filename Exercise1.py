# Databricks notebook source
import requests
import pandas as pd

# Step 1: API URL
url = "https://run.mocky.io/v3/0ff9b004-fb7a-4d8a-9c95-43f96080d0e6"

# Step 2: Make the API call
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    # Step 3: Parse JSON response
    data = response.json()
    
    # Step 4: Load JSON data into a pandas DataFrame
    df = pd.DataFrame(data)
    
    # Step 5: Save the DataFrame to a CSV file
    df.to_csv("api_data.csv", index=False)
    
    print("Data saved to api_data.csv")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
