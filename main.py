import pandas as pd
data = pd.read_csv("student_data.csv")
print("MISSING VALUES:")
print(data.isnull().sum())