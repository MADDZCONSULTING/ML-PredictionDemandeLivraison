from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from model.trainings import retrain_demande_prediction

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\PC Asus\\PycharmProjects\\DeliveryRatePrediction_11\\test.sqlite'
db = SQLAlchemy(app)

from app.invalid_usage import InvalidUsage
from app.validation import validate_livraison, validate_demande
from model.predictions import get_prediction_livraison, get_prediction_demande
from db.data_access import *

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route('/')
def index() -> str:
    # transform a dict into an application/json response
    return jsonify({"message": "It Works"})


@app.route('/predict_livraison', methods=['POST'])
def predict_livraison():
    errors = validate_livraison(request)
    if errors is not None:
        print(errors)
        raise InvalidUsage(errors)
    day = request.json.get("day", None)
    month = request.json.get("month", None)
    hub = request.json.get("hub", None)
    commune = request.json.get("commune", None)
    performance = request.json.get("performance", None)
    livraison = [[day, month, hub, commune, performance]]
    return jsonify({'prediction': get_prediction_livraison(livraison)})


@app.route('/get_demande_reelle', methods=['POST'])
def get_demande_reelle():
    errors = validate_demande(request)
    if errors is not None:
        print(errors)
        raise InvalidUsage(errors)
    debut = request.json.get("debut", None)
    fin = request.json.get("fin", None)
    if fin is None:
        return jsonify({'demande': get_demande_jour(debut)})
    else:
        return jsonify({'demande': get_demande_intervalle(debut, fin)})


@app.route('/get_demande_predite', methods=['POST'])
def get_demande_predite():
    errors = validate_demande(request)
    if errors is not None:
        print(errors)
        raise InvalidUsage(errors)
    debut = request.json.get("debut", None)
    fin = request.json.get("fin", None)
    if fin is None:
        return jsonify({'demande': get_demande_predite_jour(debut)})
    else:
        return jsonify({'demande': get_demande_predite_intervalle(debut, fin)})

@app.route('/retrain_predict', methods=['GET'])
def retrain_predict():
    dataframe = get_historique_demande_reelle()
    retrain_demande_prediction(dataframe)
    prediction = get_prediction_demande()
    set_demande_predite(prediction)
    return jsonify({'message': "done"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
