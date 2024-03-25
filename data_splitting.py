import os
import shutil
import random

# Set up directories
image_dir = "cropped_dataset"
train_dir = "dataset/train"
test_dir = "dataset/test"
test_split = 0.2

# Create train and test directories if they don't exist
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Get list of image files
image_files = os.listdir(image_dir)
random.shuffle(image_files)

# Calculate number of images for train and test
num_test = int(len(image_files) * test_split)
num_train = len(image_files) - num_test

# Move files to train and test directories
for i, image_file in enumerate(image_files):
    if i < num_test:
        shutil.move(os.path.join(image_dir, image_file), os.path.join(test_dir, image_file))
    else:
        shutil.move(os.path.join(image_dir, image_file), os.path.join(train_dir, image_file))

print(f"Successfully split data! Train: {num_train}, Test: {num_test}")
