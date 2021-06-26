import pytest
from flask import Flask, request

from src.app.validation import validate_livraison

app = Flask(__name__)


@pytest.mark.parametrize("params", [
    {"day": "1", "month": 1, "hub": 1, "commune": 1, "performance": 0.1},
    {"day": 1, "month": [1], "hub": 1, "commune": 1, "performance": 0.1},
])
def test_invalid_types_are_rejected(params, create_valid_livraison_request):
    json_input = create_valid_livraison_request(**params)
    with app.test_request_context('/', json=json_input):
        errors = validate_livraison(request)
        assert errors is not None


@pytest.mark.parametrize("required_parm_name", ["performance"])
def test_missing_required_params_is_rejected(required_parm_name, create_valid_livraison_request):
    json_input = create_valid_livraison_request()
    del json_input[required_parm_name]
    with app.test_request_context('/', json=json_input):
        errors = validate_livraison(request)
        assert errors is not None


def test_valid_livraison_is_accepted(create_valid_livraison_request):
    json_input = create_valid_livraison_request(day=1, month=1, hub=1, commune=1, performance=0.1)
    with app.test_request_context('/', json=json_input):
        errors = validate_livraison(request)
        assert errors is None
