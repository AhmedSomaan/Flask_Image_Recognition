# test_integration_sad.py

from io import BytesIO


def test_missing_file(client):
    """Test the prediction route with a missing file."""
    response = client.post("/prediction", data={}, content_type="multipart/form-data")
    assert response.status_code == 200
    assert b"File cannot be processed." in response.data  # Check if the error message is displayed


def test_empty_uploaded_file_is_handled(client):
    """Test that an uploaded file with no content returns the error response."""
    response = client.post(
        "/prediction",
        data={"file": (BytesIO(b""), "")},
        content_type="multipart/form-data"
    )

    assert response.status_code == 200
    assert b"File cannot be processed." in response.data


def test_invalid_uploaded_file_is_handled(client):
    """Test that a non-image upload returns the error response."""
    response = client.post(
        "/prediction",
        data={"file": (BytesIO(b"not an image"), "invalid.txt")},
        content_type="multipart/form-data"
    )

    assert response.status_code == 200
    assert b"File cannot be processed." in response.data
