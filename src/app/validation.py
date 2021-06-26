from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema

livraison_schema = {
    'type': 'object',
    'properties': {
        'day': {
            'type': 'integer',
        },
        'month': {
            'type': 'integer',
        },
        'hub': {
            'type': 'integer',
        },
        'commune': {
            'type': 'integer',
        },
        'performance': {
            'type': 'number',
        }
    },
    'required': ['day', 'month', 'hub', 'commune', 'performance']
}


class LivraisonInputs(Inputs):
    json = [JsonSchema(schema=livraison_schema)]


def validate_livraison(request):
    inputs = LivraisonInputs(request)
    if inputs.validate():
        return None
    else:
        return inputs.errors


demande_schema = {
    'type': 'object',
    'properties': {
        'debut': {
            'type': 'string',
            'format': 'date'
        },
        'fin': {
            'type': 'string',
            'format': 'date'
        }
    },
    'required': ['debut']
}


class DemandeInputs(Inputs):
    json = [JsonSchema(schema=demande_schema)]


def validate_demande(request):
    inputs = DemandeInputs(request)
    if inputs.validate():
        return None
    else:
        return inputs.errors
