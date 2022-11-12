from flask import Blueprint, request, jsonify
from app.models.UserType import *
from flask_cors import cross_origin

usertype = Blueprint('usertype', __name__, url_prefix='/usertype')

@usertype.route('/create_user_type', methods=['POST'])
@cross_origin()
def create_user_type():
    print(request.json)
    ust_name = request.json['ust_name']

    new_usertype = User_type(ust_name)
    
    db.session.add(new_usertype)
    db.session.commit()

    return user_type_schema.jsonify(new_usertype)

@usertype.route('/users_type', methods=['POST'])
@cross_origin()
def users_type():
    all_users_type = User_type.query.all()
    result = users_type_schema.dump(all_users_type)

    return jsonify(result)

@usertype.route('/update_user_type/<ust_id>', methods=['POST'])
@cross_origin()
def update_user_type(ust_id):
    user_type = User_type.query.get(ust_id)
    name = request.json['ust_name']

    user_type.ust_name = name
    
    db.session.commit()
    return user_type_schema.jsonify(user_type)

@usertype.route('/delete_user_type/<int:ust_id>', methods=['POST'])
@cross_origin()
def delete_user_type(ust_id):
    user_type = User_type.query.get(ust_id)
    
    db.session.delete(user_type)
    db.session.commit()

    return user_type_schema.jsonify(user_type)

@usertype.route('/select_user_type/<int:ust_id>', methods=['POST'])
@cross_origin()
def select_user_type(ust_id):
    user_type = User_type.query.get(ust_id) 
    return user_type_schema.jsonify(user_type)

