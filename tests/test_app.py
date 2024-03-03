import json

import pytest

from src.app import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

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
    res = client.get(
        "/count-words", query_string={"sentence": "Hello World from IV-SI-3!"}
    )
    assert res.status_code == 200
    assert int(res.data) == 4


def test_factorize_number(client):
    res = client.get("/factorize", query_string={"number": 75})
    assert res.status_code == 200
    assert res.json == [3, 5, 5]


def test_factorize_number_without_number(client):
    res = client.get("/factorize")
    assert res.status_code == 400
    assert res.json == {"message": "Missing parameter: number"}


def test_number_of_digits(client):
    res = client.get("/number-of-digits", query_string={"number": 75})
    assert res.status_code == 200
    assert int(res.data) == 2


def test_number_of_digits_without_number(client):
    res = client.get("/number-of-digits")
    assert res.status_code == 400
    assert res.json == {"message": "Missing parameter: number"}


def test_post_question(client):
    question = {
        "question": "What is the answer to life, the universe, and everything?",
        "answer": 42,
        "dummies": ["Family", "Love", "Health"],
    }

    res = client.post("/question", json=question)
    assert res.status_code == 201


def test_get_question(client):
    res = client.get("/question")
    assert res.status_code == 200
    assert len(res.json) > 0


def test_get_question_by_id(client):
    res = client.get("/question/5")
    assert res.status_code == 200


def test_delete_question_by_id(client):
    res = client.delete("/question/5")
    assert res.status_code == 200


def test_delete_question_by_id_not_found(client):
    res = client.delete("/question/100")
    assert res.status_code == 404


def test_put_question_by_id(client):
    question = {
        "question": "What is the answer to life, the universe, and everything?",
        "answer": 43,
        "dummies": ["Family", "Love", "Health"],
    }

    res = client.put("/question/1", json=question)
    assert res.status_code == 200


def test_put_question_by_id_not_found(client):
    question = {
        "question": "What is the answer to life, the universe, and everything?",
        "answer": 43,
        "dummies": ["Family", "Love", "Health"],
    }

    res = client.put("/question/100", json=question)
    assert res.status_code == 404


def test_user_register_success(client):
    res = client.post("/register", data={"username": "test", "password": "test"})
    assert res.status_code == 201

    # brisemo da bi test mogao da se ponovi
    res = client.delete("/user", json={"username": "test"})
    assert res.status_code == 200


def test_user_register_fail(client):
    res = client.post("/register", data={"username": "test", "password": "test"})
    assert res.status_code == 201

    res = client.post("/register", data={"username": "test", "password": "test"})
    assert res.status_code == 409

    res = client.delete("/user", json={"username": "test"})


def test_user_login_success(client):
    res = client.post("/login", data={"username": "test", "password": "test"})
    assert res.status_code == 200


def test_user_login_fail(client):
    res = client.post("/login", data={"username": "test", "password": "wrong"})
    assert res.status_code == 401
