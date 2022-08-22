import os
import pickle
import pandas as pd

import requests
from flask import Flask, request, jsonify

from pymongo import MongoClient

MODEL_FILE = os.getenv('MODEL_FILE', 'model.pkl')

EVIDENTLY_SERVICE_ADDRESS = os.getenv('EVIDENTLY_SERVICE', 'http://127.0.0.1:5000')
MONGODB_ADDRESS = os.getenv("MONGODB_ADDRESS", "mongodb://127.0.0.1:27017")

with open(MODEL_FILE, "rb") as model_file:
    churn_model = pickle.load(model_file)

app = Flask('churn-prediction')
mongo_client = MongoClient(MONGODB_ADDRESS)
db = mongo_client.get_database("prediction_service")
collection = db.get_collection("data")
    
@app.route('/predict', methods = ['POST'])
def predict_endpoint():
    customer = request.get_json()

    features = customer.copy()
    features["TotalCharges"] = "0" if features["TotalCharges"] == " " else features["TotalCharges"]
    record = features.copy()
    features = pd.DataFrame([features])
    
    churn_pred = churn_model.predict(features)

    result = {
        'churn_prediction': int(churn_pred)
    }

    print(result)
    
    save_to_db(record, int(churn_pred))
    send_to_evidently_service(record, int(churn_pred))
    return jsonify(result)

def save_to_db(record, prediction):
    rec = record.copy()
    rec['prediction'] = prediction
    collection.insert_one(rec)


def send_to_evidently_service(record, prediction):
    rec = record.copy()
    rec['prediction'] = prediction
    requests.post(f"{EVIDENTLY_SERVICE_ADDRESS}/iterate/customer", json = [rec])

if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0', port = 9696)
    
    
    