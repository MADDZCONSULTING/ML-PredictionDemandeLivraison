from prophet import Prophet
import json
from prophet.serialize import model_to_json

def retrain_demande_prediction(dataframe):
    model = Prophet(changepoint_range=0.95)
    model.fit(dataframe)
    with open('src/app/serialized_model.json', 'w') as fout:
        json.dump(model_to_json(model), fout)
