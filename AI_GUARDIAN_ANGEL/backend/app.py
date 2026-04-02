from flask import Flask, request, jsonify
from flask_cors import CORS          
from predictor import predict_score
from ai_engine import generate_suggestion

app = Flask(__name__)                
CORS(app)                             

@app.route("/")
def home():
    return "AI Guardian Angel Backend Running "

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    sleep = data["sleep"]
    steps = data["steps"]
    voice = data["voice"]
    meal = data["meal"]

    score = predict_score(sleep, steps, voice, meal)
    suggestion = generate_suggestion(score)
    
    return jsonify({
        "independence_score": score,
        "suggestion": suggestion
    })

if __name__ == "__main__":
    app.run(debug=True)