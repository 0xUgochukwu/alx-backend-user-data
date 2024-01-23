#!/usr/bin/env python3
""" Flask App
"""
from flask import Flask, jsonify, request, abort
from os import getenv
from auth import Auth


app = Flask(__name__)
app.url_map.strict_slashes = False
AUTH = Auth()


@app.route("/", methods=["GET"])
def hello() -> str:
    """ GET /
        Return:
          - JSON payload
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register_user() -> str:
    """ POST /users
        Return:
          - JSON payload
    """
    try:
        email = request.form["email"]
        password = request.form["password"]
    except KeyError:
        abort(400)

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"])
def log_in() -> str:
    """ POST /sessions
        Return:
          - JSON payload
    """
    try:
        email = request.form["email"]
        password = request.form["password"]
    except KeyError:
        abort(400)

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response
    else:
        abort(401)


if __name__ == "__main__":
    port = getenv("API_PORT") or 5000
    host = getenv("API_HOST") or "0.0.0.0"
    app.run(host=host, port=port)
