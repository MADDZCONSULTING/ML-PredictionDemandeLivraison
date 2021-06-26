def test_info(client):
    response = client.get('/')
    result = response.get_json()
    assert result is not None
    assert "message" in result
    assert result["message"] == "It Works"


def test_predict_livraison(client):
    request_payload = {"day": 1, "month": 1, "hub": 1, "commune": 1, "performance": 0.1}
    response = client.post("/predict_livraison", json=request_payload)
    result = response.get_json()

    assert response.status_code == 200
    assert result is not None
    assert "prediction" in result
    assert result['prediction'] == 0


def test_prediction_requires_greetee(client):
    request_payload = {}
    response = client.post("/predict_livraison", json=request_payload)
    result = response.get_json()

    assert response.status_code == 400
    assert result is not None
    assert "message" in result
    assert "is a required property" in result['message'][0]
