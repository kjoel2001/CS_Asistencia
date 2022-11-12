from flask import Blueprint, request, jsonify
from app.models.Teacher import *
from flask_cors import cross_origin

teacher = Blueprint('teacher', __name__, url_prefix='/teacher')

@teacher.route('/create_teacher', methods=['POST'])
@cross_origin()
def create_teacher():
    print(request.json)

    usr_id   = request.json['usr_id']
    tea_type = request.json['tea_type']
    tea_cat  = request.json['tea_cat']

    new_teacher = Teacher(tea_cat, tea_type, usr_id)
    db.session.add(new_teacher)
    db.session.commit()

    return teacher_schema.jsonify(new_teacher)

@teacher.route('/teachers', methods=['POST'])
@cross_origin()
def teachers():
    all_teachers = Teacher.query.all()
    result = teachers_schema.dump(all_teachers)
    return jsonify(result)

@teacher.route('/update_teacher/<int:tea_id>', methods=['POST'])
@cross_origin()
def update_teacher(tea_id):
    teacher = teacher.query.get(tea_id)
    
    tea_cat = request.json['tea_cat']
    tea_type = request.json['tea_type']

    teacher.tea_cat = tea_cat
    teacher.tea_type = tea_type
    
    db.session.commit()
    return teacher_schema.jsonify(teacher)

@teacher.route('/delete_teacher/<int:tea_id>', methods=['POST'])
@cross_origin()
def delete_teacher(tea_id):
    teacher = teacher.query.get(tea_id)
    
    db.session.delete(teacher)
    db.session.commit()

    return teacher_schema.jsonify(teacher)

@teacher.route('/select_teacher/<int:tea_id>', methods=['POST'])
@cross_origin()
def select_teacher(tea_id):
    teacher = teacher.query.get(tea_id) 

    return teacher_schema.jsonify(teacher)

