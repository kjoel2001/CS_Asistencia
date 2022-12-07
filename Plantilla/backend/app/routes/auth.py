from re import split
from flask import Blueprint, request, jsonify
from app.auth.flask_auth_jwt import write_token, validate_token
from collections.abc import Mapping


routes_auth = Blueprint("routes_auth", __name__)


@routes_auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if data['username'] == "Nelson Hernandez":
        return write_token(data=request.get_json())
    else:
        response = jsonify({"message": "User not found"})
        response.status_code = 404
        return response

@routes_auth.route("/verify/token")
def verify():
    token = request.headers['Authorization'].split(" ")[1]
    return validate_token(token, output=True)