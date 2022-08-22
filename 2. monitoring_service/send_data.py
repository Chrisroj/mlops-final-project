import json
import uuid
from datetime import datetime
from time import sleep

#import pyarrow.parquet as pq
import pandas as pd
import requests

df = pd.read_csv("test_set.csv")
data_target = df[target_name].tolist()
data_features = df.drop(target_name, axis = 1).to_dict('records')


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)

with open("target.csv", 'w') as f_target:
    for row, target in zip(data_features, data_target):
        row['id'] = str(uuid.uuid4())
        f_target.write(f"{row['id']},{target}\n")
        resp = requests.post("http://127.0.0.1:9696/predict",
                             headers={"Content-Type": "application/json"},
                             data=json.dumps(row, cls=DateTimeEncoder)).json()
        print(f"prediction: {resp['churn_prediction']}")
        sleep(1)
