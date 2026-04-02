import joblib
import numpy as np

# Load trained model
model = joblib.load("../model/model.pkl")

def predict_score(sleep, steps, voice, meal):
    data = np.array([[sleep, steps, voice, meal]])
    prediction = model.predict(data)
    return round(prediction[0], 2)