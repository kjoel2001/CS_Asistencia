from flask import Blueprint, request, jsonify
from app.models.Student import *
from flask_cors import cross_origin

student = Blueprint('student', __name__, url_prefix='/student')

@student.route('/create_student', methods=['POST'])
@cross_origin()
def create_student():
    print(request.json)
    
    usr_id      = request.json['usr_id']
    std_year    = request.json['std_year']
    std_regular = request.json['std_regular']

    new_student = Student(std_regular, std_year, usr_id)
    
    db.session.add(new_student)
    db.session.commit()

    return student_schema.jsonify(new_student)

@student.route('/students', methods=['POST'])
@cross_origin()
def students():
    all_students = student.query.all()
    result = students_schema.dump(all_students)
    return jsonify(result)

@student.route('/update_student/<int:std_id>', methods=['POST'])
@cross_origin()
def update_student(std_id):
    student = student.query.get(std_id)
    
    std_regular = request.json['std_regular']
    student.std_regular = std_regular
    
    db.session.commit()
    return student_schema.jsonify(student)

@student.route('/delete_student/<int:std_id>', methods=['POST'])
@cross_origin()
def delete_student(std_id):
    student = student.query.get(std_id)
    
    db.session.delete(student)
    db.session.commit()

    return student_schema.jsonify(student)

@student.route('/select_student/<int:std_id>', methods=['POST'])
@cross_origin()
def select_student(std_id):
    student = student.query.get(std_id) 

    return student_schema.jsonify(student)

