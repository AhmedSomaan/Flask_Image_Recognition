# test_integration_happy.py

from io import BytesIO
import re


def test_home_page_accessible(client):
    """Test that the Flask home page can be accessed successfully."""
    response = client.get("/")

    assert response.status_code == 200
    assert b"Hand Sign Digit Language Detection" in response.data


def test_valid_request_produces_expected_response(client):
    """Test that a valid image request returns a digit prediction."""
    image_path = "test_images/2/Sign 2 (97).jpeg"

    with open(image_path, "rb") as image_file:
        response = client.post(
            "/prediction",
            data={"file": (image_file, "Sign 2 (97).jpeg")},
            content_type="multipart/form-data"
        )

    assert response.status_code == 200
    assert b"Prediction" in response.data
    assert re.search(rb"<h2[^>]*>\d+</h2>", response.data)


def test_successful_prediction(client):
    """Test the successful image upload and prediction."""
    # Create a mock image file with minimal valid content
    img_data = BytesIO(b"fake_image_data")
    img_data.name = "test.jpg"

    # Simulate a file upload to the correct prediction endpoint
    response = client.post(
        "/prediction",  # Correct route for prediction
        data={"file": (img_data, img_data.name)},
        content_type="multipart/form-data"
    )

    # Assertions
    assert response.status_code == 200
    assert b"Prediction" in response.data  # Modify this check based on your output
