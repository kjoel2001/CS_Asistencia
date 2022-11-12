from flask import Blueprint, request, jsonify
from app.models.Group import *
from flask_cors import cross_origin

group = Blueprint('group', __name__, url_prefix='/group')

@group.route('/create_group', methods=['POST'])
@cross_origin()
def create_group():
    print(request.json)
    gro_name = request.json['gro_name']
    cur_id   = request.json['cur_id']
    tea_id   = request.json['tea_id']

    new_group = Group(gro_name, cur_id, tea_id)
    
    db.session.add(new_group)
    db.session.commit()

    return group_schema.jsonify(new_group)

@group.route('/groups', methods=['POST'])
@cross_origin()
def groups():
    all_groups = Group.query.all()
    result = groups_schema.dump(all_groups)
    return jsonify(result)

@group.route('/update_group/<int:gru_id>', methods=['POST'])
@cross_origin()
def update_group(gru_id):
    group = Group.query.get(gru_id)
    
    gru_name = request.json['gru_name']
    cur_id = request.json['cur_id']
    tea_id = request.json['tea_id']

    group.gru_name = gru_name
    group.tea_id = tea_id
    group.cur_id = cur_id
    
    db.session.commit()
    return group_schema.jsonify(group)

@group.route('/delete_group/<int:gru_id>', methods=['POST'])
@cross_origin()
def delete_group(gru_id):
    group = Group.query.get(gru_id)
    
    db.session.delete(group)
    db.session.commit()

    return group_schema.jsonify(group)

@group.route('/select_group/<int:gru_id>', methods=['POST'])
@cross_origin()
def select_group(gru_id):
    group = Group.query.get(gru_id) 

    return group_schema.jsonify(group)

