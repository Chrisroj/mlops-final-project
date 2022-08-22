import pickle
import pandas as pd

from flask import Flask, request, jsonify

with open("model.pkl", "rb") as model_file:
    churn_model = pickle.load(model_file)
    
def features_preparation(customer):
    features = customer.copy()
    features["TotalCharges"] = "0" if features["TotalCharges"] == " " else features["TotalCharges"]
    return features
    
def predict(features):
    churn_pred = churn_model.predict(features)
    return int(churn_pred) 
    
app = Flask('churn-prediction')
    
@app.route('/predict', methods = ['POST'])
def predict_endpoint():
    customer = request.get_json()

    features = features_preparation(customer)
    features = pd.DataFrame([features])
    churn_pred = predict(features)

    result = {
        'churn_prediction': churn_pred
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0', port = 9696)
    
    
    