import os
import pandas as pd

from sklearn.model_selection import train_test_split

RANDOM_STATE = 12354

data_folder = os.path.join(os.getcwd(), "0. data")
eda_folder = os.path.join(os.getcwd(), "1. eda_and_modeling", "data")
datasets_evidently_folder = os.path.join(os.getcwd(), "3. monitoring", "evidently_service", "datasets")
data_file_path = os.path.join(data_folder, "WA_Fn-UseC_-Telco-Customer-Churn.csv")

data = pd.read_csv(data_file_path)

# Preprocess Target
data["Churn"] = data["Churn"].replace({"No": 0, "Yes": 1})

# Split Data
train_set, test_set = train_test_split(data, test_size = 0.25, stratify = data["Churn"], random_state = RANDOM_STATE)

# Save Data
print("Saving Train Set...")
train_set.to_csv(os.path.join(eda_folder, "train_set.csv"), index = False, encoding = "utf-8")
test_set.to_csv(os.path.join(datasets_evidently_folder, "train_set.csv"), index = False, encoding = "utf-8")
print("Saving Test Set...")
test_set.to_csv(os.path.join(eda_folder, "test_set.csv"), index = False, encoding = "utf-8")
test_set.to_csv(os.path.join(os.getcwd(), "3. monitoring", "test_set.csv"), index = False, encoding = "utf-8")
