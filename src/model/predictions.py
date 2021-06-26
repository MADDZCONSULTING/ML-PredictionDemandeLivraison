import json
import pickle

from prophet.serialize import model_from_json


def get_prediction_livraison(livraison):
    filename = "src/app/model.sav"
    loaded_model = pickle.load(open(filename, 'rb'))
    return int(loaded_model.predict(livraison))


def get_prediction_demande():
    filename = "src/app/serialized_model.json"
    model = model_from_json(json.load(open(filename, 'rb')))
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)
    return forecast[['ds', 'yhat']].tail(30)
