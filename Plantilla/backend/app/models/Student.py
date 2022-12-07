from app import db, ma
from .User import User
from flask import jsonify, request

class Student(db.Model):
    __tablename__ = 'student'
    
    std_id      = db.Column(db.Integer, primary_key=True)
    std_regular = db.Column(db.Boolean)
    std_year    = db.Column(db.Date())

    usr_id = db.Column(db.Integer, db.ForeignKey(User.usr_id))

    def __init__(self, std_regular=None, std_year=None, usr_id=None):
        self.std_regular = std_regular
        self.std_year    = std_year
        self.usr_id      = usr_id

    def create_student(self, usr_id, std_year, std_regular):
        new_student = Student(std_regular, std_year, usr_id)

        db.session.add(new_student)
        db.session.commit()
        return student_schema.jsonify(new_student)

    def students(self):
        all_students = Student.query.all()
        result = students_schema.dump(all_students)
        return result

    def update_student(self, std_id, std_regular):
        student = Student.query.get(std_id)

        student.std_regular = std_regular
        db.session.commit()
        return student_schema.jsonify(student)

    def delete_student(self, std_id):
        student = Student.query.get(std_id)
        db.session.delete(student)
        db.session.commit()
        return student_schema.jsonify(student)  

    def select_student(self, std_id):
        student = Student.query.get(std_id) 
        return student_schema.jsonify(student)

class StudentSchema(ma.Schema):
    class Meta:
        fields = (
            'std_id',
            'std_regular',
            'std_year',
            'usr_id'
        )

student_schema  = StudentSchema()
students_schema = StudentSchema(many=True)