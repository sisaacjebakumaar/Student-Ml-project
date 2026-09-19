import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 

data = pd.read_csv("student_data.csv")

X = data[[
    "Study_Hours",
    "Attendance",
    "Previous_Mark",
    "Assignment"
]]

y =data["Final_Mark"]

print("Input Features (X):")
print(X)

print("\nTarget:")
print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train,y_train)
print("Model training finished.")

predictions = model.predict(X_test)

results = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": predictions
})

print(results)

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, predictions)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)

# New student data
new_student = pd.DataFrame({
    "Study_Hours": [6],
    "Attendance": [85],
    "Previous_Mark": [75],
    "Assignment": [80]
})

# Predict final mark
predicted_mark = model.predict(new_student)

print("Predicted Final Mark:", predicted_mark[0])