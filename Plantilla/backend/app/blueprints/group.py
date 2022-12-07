from flask import Blueprint, request, jsonify
from app.models.Group import *
from flask_cors import cross_origin

group = Blueprint('group', __name__, url_prefix='/group')
model = Group()

@group.route('/create_group', methods=['POST'])
@cross_origin()
def create_group():
    return (model.create_group(request.json['gro_name'],
                               request.json['cur_id'], 
                               request.json['tea_id']))

@group.route('/groups', methods=['GET'])
@cross_origin()
def groups():
    return jsonify(model.groups())

@group.route('/update_group', methods=['PUT'])
@cross_origin()
def update_group():
    return (model.update_group(request.json['gru_id'],
                               request.json['gru_name'], 
                               request.json['cur_id'], 
                               request.json['tea_id']))

@group.route('/delete_group', methods=['DELETE'])
@cross_origin()
def delete_group():
    return (model.delete_group(request.json['gru_id']))

@group.route('/select_group', methods=['GET'])
@cross_origin()
def select_group():
    return (model.delete_group(request.json['gru_id']))
