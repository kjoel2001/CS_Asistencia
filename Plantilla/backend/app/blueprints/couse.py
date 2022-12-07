from flask import Blueprint, request, jsonify
from app.models.Course import *
from flask_cors import cross_origin

course = Blueprint('course', __name__, url_prefix='/course')
model = Course()

@course.route('/create_course', methods=['POST'])
@cross_origin()
def create_course():
    return (model.create_course(request.json['cur_name'], request.json['cur_des']))

@course.route('/courses', methods=['GET'])
@cross_origin()
def courses():
    return jsonify(model.courses())

@course.route('/select_course', methods=['GET'])
@cross_origin()
def select_course():
    return (model.select_course(request.json['cur_id']))

@course.route('/update_course', methods=['POST'])
@cross_origin()
def update_course():
    print("se edito")
    return (model.update_course(request.json['cur_id'],
                                request.json['cur_name'], 
                                request.json['cur_des']))

@course.route('/delete_course', methods=['POST'])
@cross_origin()
def delete_course():
    print("se borro")
    return (model.delete_course(request.json['cur_id']))
    

