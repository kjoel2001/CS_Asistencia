from app import db, ma
from .Group import Group
from .Student import Student
from flask import jsonify, request
from app.functions.openfaceAPI import openfaceAPI
from app.functions.attendance import *
from app.models.User import User
import requests

class Attendance(db.Model):
    __tablename__ = 'attendance' 
    
    att_id    = db.Column(db.Integer, primary_key=True)
    att_val   = db.Column(db.Boolean)
    att_date  = db.Column(db.Integer)
 
    gru_id    = db.Column(db.Integer, db.ForeignKey(Group.gru_id))
    std_id    = db.Column(db.Integer, db.ForeignKey(Student.std_id))
    
    def __init__(self, att_val=None, att_date=None, gru_id=None, std_id=None):
        self.att_val  = att_val
        self.att_date = att_date
        self.gru_id   = gru_id
        self.std_id   = std_id

    def marck_attendance(self, usr_dni):
        # File photo
        f = request.files['file']
        user = User.query.filter_by(usr_dni=usr_dni).first_or_404()
        # Save photo for processing and return path
        path = savePath(f)
        # call openfaceAPI, return vector de caracteristicas ##################################
        result = openfaceAPI(path)

        vector1 = []
        vector2 = []
        # Procesamos los datos para trabajr con ellos
        vector1 = toFloat(dictToString(result))
        vector2 = toFloat(toString(user['usr_vec']))
        return (marckAttendanc(vector1, vector2))

    def create_attendance(self, file, data={}):
        f = request.files['file']

        if marckAttendanc(file, data['usr_dni']):
            att_val  = data['att_val']
            att_date = data['att_date']
            gru_id   = data['gru_id']
            std_id   = data['std_id']

            new_attendance = Attendance(att_val, att_date, gru_id, std_id)
            db.session.add(new_attendance)
            db.session.commit()
            return attendance_schema.jsonify(new_attendance)
        
        else:
            return "Error"

    def attendances(self):
        all_attendances = Attendance.query.all()
        result = attendances_schema.dump(all_attendances)
        return jsonify(result)

    def update_attendance(self, att_id, att_val, att_date):
        attendance = Attendance.query.get(att_id)

        attendance.att_val = att_val
        attendance.att_date = att_date

        db.session.commit()
        return attendance_schema.jsonify(attendance)

    def delete_attendance(self, att_id):
        attendance = Attendance.query.get(att_id)
        db.session.delete(attendance)
        db.session.commit()
        return attendance_schema.jsonify(attendance)

    def select_attendance(self, att_id):
        attendance = Attendance.query.get(att_id) 
        return attendance_schema.jsonify(attendance)

class AttendanceSchema(ma.Schema):
    class Meta:
        fields = (
            'att_id',
            'att_val',
            'att_date',
            'gru_id',
            'std_id'
        )

attendance_schema  = AttendanceSchema()
attendances_schema = AttendanceSchema(many=True)
