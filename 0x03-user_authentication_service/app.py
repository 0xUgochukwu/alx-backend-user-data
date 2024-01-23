#!/usr/bin/env python3
""" Flask App
"""
from flask import Flask, jsonify
from os import getenv


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello() -> str:
    """ GET /
        Return:
          - JSON payload
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    port = getenv("API_PORT") or 5000
    host = getenv("API_HOST") or "0.0.0.0"
    app.run(host=host, port=port)
