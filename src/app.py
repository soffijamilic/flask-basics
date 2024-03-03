import os

from flask import Flask, request

import src.data as dal  # data access layer
import src.functions as f


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route("/")
    def hello():
        return "Hello, World!"

    @app.route("/count-words", methods=["GET"])
    def count_words():
        sentence = request.args.get("sentence")
        if sentence is None:
            return b"0"
        return str(len(sentence.split()))

    @app.route("/factorize", methods=["GET"])
    def factorize():
        number = request.args.get("number")
        if number is None:
            return {"message": "Missing parameter: number"}, 400
        return f.factorize(int(number))

    @app.route("/number-of-digits", methods=["GET"])
    def number_of_digits():
        number = request.args.get("number")
        if number is None:
            return {"message": "Missing parameter: number"}, 400
        return str(f.number_of_digits(int(number)))

    @app.route("/question", methods=["GET", "POST"])
    def question():

        if request.method == "GET":
            questions = dal.get_questions()
            return questions.to_dict(orient="records")

        if request.method == "POST":
            json = request.json
            json["dummies"] = "|".join(json["dummies"])
            dal.add_question(json)
            return "Created", 201

    @app.route("/question/<int:id>", methods=["GET"])
    def get_question(id):
        question = dal.get_questions(id)
        return question.to_dict()

    return app
