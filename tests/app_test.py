import pytest
from app import app


@pytest.fixture
def client():
    tester = app.test_client()
    yield tester


def test_index(client):
    response = client.get("/", content_type="html/text")
    assert response.status_code == 200