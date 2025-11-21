"""
01_train_val_test_split.py
Purpose:
    Create train/validation/test split using *raw JPGs*.
    Skips "Formalin-mixed" automatically.
    Ignores non-image files (desktop.ini, .DS_Store, etc.).
Output:
    DATA/dataset_splits/train/
    DATA/dataset_splits/val/
    DATA/dataset_splits/test/
"""

import os
import shutil
from sklearn.model_selection import train_test_split

RAW_DIR = "DATA/raw/Fruits Original"
OUTPUT_DIR = "DATA/dataset_splits"

# Make output folders
for split in ["train", "val", "test"]:
    os.makedirs(os.path.join(OUTPUT_DIR, split), exist_ok=True)


def is_image(filename):
    """Return True if file looks like a valid image."""
    return filename.lower().endswith((".jpg", ".jpeg", ".png"))


def get_all_samples():
    samples = []
    labels = []

    for fruit in os.listdir(RAW_DIR):
        fruit_path = os.path.join(RAW_DIR, fruit)

        # Skip hidden files (desktop.ini, .DS_Store)
        if not os.path.isdir(fruit_path):
            continue

        for condition in os.listdir(fruit_path):
            condition_path = os.path.join(fruit_path, condition)

            # Skip invalid or unwanted folders
            if condition.lower() == "formalin-mixed":
                continue

            if not os.path.isdir(condition_path):
                continue

            for file in os.listdir(condition_path):
                if not is_image(file):
                    continue

                file_path = os.path.join(condition_path, file)
                samples.append(file_path)
                labels.append(condition)

    return samples, labels


# Load samples
samples, labels = get_all_samples()

# Stratified split
train_s, temp_s, train_l, temp_l = train_test_split(
    samples, labels, test_size=0.30, stratify=labels, random_state=42
)

val_s, test_s, val_l, test_l = train_test_split(
    temp_s, temp_l, test_size=0.50, stratify=temp_l, random_state=42
)


def copy_split(files, split_name):
    for f in files:
        condition = os.path.basename(os.path.dirname(f))   # safe & cross-platform
        save_dir = os.path.join(OUTPUT_DIR, split_name, condition)
        os.makedirs(save_dir, exist_ok=True)
        shutil.copy(f, os.path.join(save_dir, os.path.basename(f)))


copy_split(train_s, "train")
copy_split(val_s, "val")
copy_split(test_s, "test")

print("Train/Val/Test split complete.")