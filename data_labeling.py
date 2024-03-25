import pandas as pd
import os
import re

# Define paths and variables
data_file = "cars_train_annos.csv"
image_dir = "dataset"
class_name_mapping = {
    "SUV": "delivery",
    "Truck": "delivery",
    "Sedan": "resident",
    "Coupe": "resident",
    "Hatchback": "resident",
}

# Define a function to match car class with partial string matching
def match_class_name(class_name):
    for key, value in class_name_mapping.items():
        if re.search(key, class_name, flags=re.IGNORECASE):  # Case-insensitive search
            return value
    return "other"  # Default label for unmatched classes

# Check if the data file exists
if not os.path.exists(data_file):
    print(f"Error: Data file '{data_file}' not found.")
    exit()

# Read data from CSV using pandas
try:
    data = pd.read_csv(data_file)
except Exception as e:
    print(f"Error reading CSV file: {e}")
    exit()

# Check if 'class_name' column exists
if 'class_name' not in data.columns:
    print("Error: 'class_name' column not found in the data.")
    exit()

# Add a new column named "label" based on car class with partial matching
data["label"] = data["class_name"].apply(match_class_name)

# Update the CSV file with the labeled data
try:
    data.to_csv(data_file, index=False)
    print(f"Successfully updated {data_file} with labels!")
except Exception as e:
    print(f"Error updating CSV file: {e}")
