import pytest
from src.app import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_request_example(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, World!" in response.data

def test_count_words_in_sentence(client):
    res = client.get("/count-words", query_string={"sentence": "Hello World from IV-SI-3!"})
    assert res.status_code == 200
    assert int(res.data) == 4

def test_factorize_number(client):
    res = client.get("/factorize", query_string={"number": 75})
    assert res.status_code == 200
    assert res.json == [3, 5, 5]