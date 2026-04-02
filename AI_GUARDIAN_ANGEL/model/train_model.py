import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

data = pd.read_csv("../data/elderly_data.csv")

X = data[['sleep_hours', 'steps', 'voice_interaction', 'meal_taken']]

y = data['independence_score']

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model trained successfully!")
