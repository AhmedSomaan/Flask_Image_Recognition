
import pytest
from app import app  # This imports the Flask app for testing


@pytest.fixture
def client():
    app.config.update(TESTING=True, WTF_CSRF_ENABLED=False)
    with app.test_client() as test_client:
        yield test_client
