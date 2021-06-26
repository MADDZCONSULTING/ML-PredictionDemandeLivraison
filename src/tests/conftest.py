import pytest
from src.app import main


@pytest.fixture
def client():
    main.app.config['TESTING'] = True
    client = main.app.test_client()
    yield client


@pytest.fixture()
def create_valid_livraison_request():
    """
    Helper function for creating a correctly-structured
    json request
    """

    def _create_valid_livraison_request(day=1, month=1, hub=1, commune=1, performance=0.1):
        return {
            "day": day,
            "month": month,
            "hub": hub,
            "commune": commune,
            "performance": performance
        }

    return _create_valid_livraison_request
