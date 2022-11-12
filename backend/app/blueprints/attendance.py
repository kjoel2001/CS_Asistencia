from flask import Blueprint, request, jsonify
from app.models.Attendance import *
from flask_cors import cross_origin
import requests
from app.functions.openfaceAPI import openfaceAPI
from app.functions.attendance import *
from os import remove


attendance = Blueprint('attendance', __name__, url_prefix='/attendance')

@attendance.route('/marck_attendace/<usr_dni>', methods=['POST'])
def marck_attendance(usr_dni):
    # File photo
    f = request.files['file']
            
    # Call endpoint /user/select_dni/<usr_dni> -> Return user 
    url  = f'http://127.0.0.1:5000/user/select_dni/{usr_dni}'
    user = requests.post(url)
    user = user.json()
    # print(user.json())
    
    # Save photo for processing and return path
    path = savePath(f)

    # call openfaceAPI, return vector de caracteristicas ##################################
    result = openfaceAPI(path)

    vector1 = []
    vector2 = []
    
    # Procesamos los datos para trabajr con ellos
    vector1 = toFloat(dictToString(result))
    vector2 = toFloat(toString(user['usr_vec']))
    
    print(marckAttendanc(vector1, vector2))
    # print(result.json())

    # Phoyo deleted
    remove(path)

    return "OK"


@attendance.route('/create_attendance', methods=['POST'])
@cross_origin()
def create_attendance():
    f = request.files['file']

    att_val  = request.json['att_val']
    att_date = request.json['att_date']
    gru_id   = request.json['gru_id']
    std_id   = request.json['std_id']

    new_attendance = attendance(att_val, att_date, gru_id, std_id)
    
    db.session.add(new_attendance)
    db.session.commit()
    return attendance_schema.jsonify(new_attendance)


@attendance.route('/attendances', methods=['POST'])
@cross_origin()
def attendances():
    all_attendances = attendance.query.all()
    result = attendances_schema.dump(all_attendances)
    return jsonify(result)


@attendance.route('/update_attendance/<int:att_id>', methods=['POST'])
@cross_origin()
def update_attendance(att_id):
    attendance = attendance.query.get(att_id)
    
    att_val  = request.json['att_val']
    att_date = request.json['att_date']

    attendance.att_val = att_val
    attendance.att_date = att_date
    
    db.session.commit()
    return attendance_schema.jsonify(attendance)


@attendance.route('/delete_attendance/<int:att_id>', methods=['POST'])
@cross_origin()
def delete_attendance(att_id):
    attendance = attendance.query.get(att_id)
    
    db.session.delete(attendance)
    db.session.commit()
    return attendance_schema.jsonify(attendance)


@attendance.route('/select_attendance/<int:att_id>', methods=['POST'])
@cross_origin()
def select_attendance(att_id):
    attendance = attendance.query.get(att_id) 
    return attendance_schema.jsonify(attendance)

