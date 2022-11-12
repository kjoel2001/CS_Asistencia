from flask import Blueprint, request, jsonify
from app.models.Course import *
from flask_cors import cross_origin

course = Blueprint('course', __name__, url_prefix='/course')

@course.route('/create_course', methods=['POST'])
@cross_origin()
def create_course():
    print(request.json)

    cur_name = request.json['cur_name']
    cur_des  = request.json['cur_des']

    new_course = Course(cur_name,cur_des)
    db.session.add(new_course)
    db.session.commit()

    return course_schema.jsonify(new_course)

#ver cursos
@course.route('/courses', methods=['POST'])
@cross_origin()
def courses():
    all_courses = Course.query.all()
    result = courses_schema.dump(all_courses)
    return jsonify(result)

#buscar curso por id
@course.route('/select_course/<int:cur_id>', methods=['POST'])
@cross_origin()
def select_course(cur_id):
    course = Course.query.get(cur_id)
    return course_schema.jsonify(course)

@course.route('/update_course/<int:cur_id>', methods=['POST'])
@cross_origin()
def update_course(cur_id):
    course = Course.query.get(cur_id)
    cur_name = request.json['cur_name']
    cur_des = request.json['cur_des']

    course.cur_name = cur_name
    course.cur_des = cur_des

    db.session.commit()
    return course_schema.jsonify(course)

@course.route('/delete_course/<cur_id>', methods=['POST'])
@cross_origin()
def delete_course(cur_id):
    course = Course.query.get(cur_id)
    db.session.delete(course)
    db.session.commit()
    return course_schema.jsonify(course)