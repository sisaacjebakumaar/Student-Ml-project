import pandas as pd
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