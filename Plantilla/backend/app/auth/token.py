from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from flask import Blueprint, request, jsonify
from app.models.User import *
from app import app

login_web_token = Blueprint('token', __name__)

@app.route("/token", methods=["POST"])
def create_token():
    #username = request.json.get("username", None)
    #password = request.json.get("password", None)
        
    data = request.get_json()
    username = data["usr_dni"]
    password = data["usr_pass"]
    print(username) 
    print(password)
    # Query your database for username and password
    user = User.query.filter_by(usr_dni=username, usr_pass=password).first()
    
    if user is None:
        # the user was not found on the database
        return jsonify({"msg": "Usuario o contraseña incorrecto"}), 401
    
    # create a new token with the user id inside
    access_token = create_access_token(identity=username)
    print(access_token)
    return jsonify({ "token": access_token, "user_id": user.usr_id })


from flask_jwt_extended import jwt_required, get_jwt_identity
# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.
@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    
    return jsonify({"id": user.id, "username": user.username }), 200