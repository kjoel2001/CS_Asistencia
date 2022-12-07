from flask import Blueprint, request, jsonify
from app.models.Student import *
from flask_cors import cross_origin

student = Blueprint('student', __name__, url_prefix='/student')
model = Student()

@student.route('/create_student', methods=['POST'])
@cross_origin()
def create_student():
    return (model.create_student(request.json['usr_id'], 
                                        request.json['std_year'], 
                                        request.json['std_regular']))

@student.route('/students', methods=['GET'])
@cross_origin()
def students():
    return jsonify(model.students())

@student.route('/update_student', methods=['PUT'])
@cross_origin()
def update_student():
    return (model.update_student(request.json['std_id'], request.json['std_regular']))

@student.route('/delete_student', methods=['DELETE'])
@cross_origin()
def delete_student():
    return (model.delete_student(request.json['std_id']))

@student.route('/select_student', methods=['GET'])
@cross_origin()
def select_student():
    return (model.select_student(request.json['std_id']))

