[7:15 PM] Toufic Fakhry
Data labeling
import pandas as pd

import os

import re
 
# Define paths and variables

data_file = "car_train_annos.csv"

image_dir = "images"  # Assuming your images reside in a folder named "images"

car_class_mapping = {

    "SUV": "delivery",

    "Truck": "delivery",

    "Sedan": "resident",

    "Coupe": "resident",

    "Hatchback": "resident",

    # Add more mappings as needed

}
 
# Define a function to match car class with partial string matching

def match_car_class(car_class):

    for key, value in car_class_mapping.items():

        if re.search(key, car_class, flags=re.IGNORECASE):  # Case-insensitive search

            return value

    return "other"  # Default label for unmatched classes
 
# Read data from CSV using pandas

data = pd.read_csv(data_file)
 
# Add a new column named "label" based on car class with partial matching

data["label"] = data["car_class"].apply(match_car_class)
 
# Update the CSV file with the labeled data

data.to_csv(data_file, index=False)
 
print(f"Successfully updated {data_file} with labels!")
