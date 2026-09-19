import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv("student_data.csv")

X = data[[
    "Study_Hours",
    "Attendance",
    "Previous_Mark",
    "Final_Mark"
]]

y =data["Final_Mark"]

print("Input Features (X):")
print(X)

print("\nTarget:")
print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\nTraining Features (X_train):")
print(X_train)

print("\nTesting Features (X_test):")
print(X_test)

print("\nTraining Target (y_train):")
print(y_train)

print("\nTesting Target (y_test):")
print(y_test)