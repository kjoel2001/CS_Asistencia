from flask import Blueprint, request, jsonify
from app.models.Teacher import *
from flask_cors import cross_origin

model = Teacher()
teacher = Blueprint('teacher', __name__, url_prefix='/teacher')

@teacher.route('/create_teacher', methods=['POST'])
@cross_origin()
def create_teacher():
    return (model.create_teacher(request.json['usr_id'],
                                 request.json['tea_type'],
                                 request.json['usr_cat']))

@teacher.route('/teachers', methods=['GET'])
@cross_origin()
def teachers():
    return jsonify(model.teachers())

@teacher.route('/update_teacher', methods=['PUT'])
@cross_origin()
def update_teacher():
    return (model.update_teacher(request.json['tea_id'], 
                                 request.json['tea_cat'], 
                                 request.json['tea_type']))

@teacher.route('/delete_teacher', methods=['DELETE'])
@cross_origin()
def delete_teacher():
    return (model.delete_teacher(request.json['tea_id']))

@teacher.route('/select_teacher', methods=['GET'])
@cross_origin()
def select_teacher():
    return (model.select_teacher(request.json['tea_id']))
