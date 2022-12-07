from flask import Blueprint, request, jsonify
from app.models.UserType import *
from flask_cors import cross_origin

model = User_type()

usertype = Blueprint('usertype', __name__, url_prefix='/usertype')

@usertype.route('/create_user_type', methods=['POST'])
@cross_origin()
def create_user_type():
    return model.create_user_type(request.json["ust_name"])

@usertype.route('/users_type', methods=['GET'])
@cross_origin()
def users_type():
    return model.users_type()

@usertype.route('/update_user_type', methods=['PUT'])
@cross_origin()
def update_user_type():
    return model.update_user_type(request.json["ust_id"], request.json["ust_name"])

@usertype.route('/delete_user_type', methods=['DELETE'])
@cross_origin()
def delete_user_type():
    return model.delete_user_type(request.json['ust_id'])

@usertype.route('/select_user_type', methods=['GET'])
@cross_origin()
def select_user_type():
    return model.select_user_type(request.json['ust_id'])

