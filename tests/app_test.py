import pytest
from app import app


@pytest.fixture
def client():
    tester = app.test_client()
    yield tester


def test_index(client):
    response = client.get("/", content_type="html/text")
    assert response.status_code == 200


def test_projects(client):
    response = client.get("/projects/", content_type="html/text")
    assert response.status_code == 200


def test_contact(client):
    response = client.get("/contact/", content_type="html/text")
    assert response.status_code == 200


def test_resume(client):
    response = client.get("/resume/", content_type="html/text")
    assert response.status_code == 200


def test_404(client):
    response = client.get("/oops/", content_type="html/text")
    assert response.status_code == 404