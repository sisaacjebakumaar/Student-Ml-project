import pandas as pd
data = pd.read_csv("student_data.csv")
print("First 5 rows of the dataset:")
print(data.head())

print("Dataset Information :")
print(data.info())

print("Summary Statistics :")
print(data.describe())