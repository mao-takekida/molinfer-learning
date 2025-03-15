"""Test route handlers for FastAPI application."""

from io import BytesIO

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from src.routes import setup_routes


@pytest.fixture
def app() -> FastAPI:
    """
    Create a test FastAPI application.

    Returns:
        FastAPI: The test application instance.

    """
    app = FastAPI()
    setup_routes(app)
    return app


@pytest.fixture
def client(app: FastAPI) -> TestClient:
    """
    Create a test client for the FastAPI application.

    Args:
        app: The FastAPI application instance.

    Returns:
        TestClient: The test client instance.

    """
    return TestClient(app)


def test_root_redirect(client: TestClient) -> None:
    """
    Test that root path redirects to API documentation.

    Args:
        client: The test client instance.

    """
    response = client.get("/", follow_redirects=False)
    expected_code = 307
    assert response.status_code == expected_code
    assert response.headers["location"] == "/docs"


def test_upload_file_success(client: TestClient) -> None:
    """
    Test successful file upload.

    Args:
        client: The test client instance.

    """
    # テスト用のファイルデータを作成
    file_content = b"test file content"
    file = BytesIO(file_content)

    response = client.post(
        "/api/file/",
        files={"file": ("test.txt", file, "text/plain")},
    )
    expected_code = 200
    assert response.status_code == expected_code
    assert response.json() == {"filename": "test.txt"}


def test_upload_file_no_file(client: TestClient) -> None:
    """
    Test file upload endpoint with no file.

    Args:
        client: The test client instance.

    """
    response = client.post("/api/file/")
    expected_code = 400
    assert response.status_code == expected_code
    assert response.json() == {"message": "No file uploaded"}
