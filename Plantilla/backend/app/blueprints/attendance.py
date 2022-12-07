from flask import Blueprint, request, jsonify
from app.models.Attendance import *
from flask_cors import cross_origin
import requests, json
from app.functions.openfaceAPI import openfaceAPI
from app.functions.attendance import *
from os import remove

model = Attendance()

attendance = Blueprint('attendance', __name__, url_prefix='/attendance')

@attendance.route('/marck_attendace', methods=['POST'])
def marck_attendance():
    return jsonify(model.marck_attendance(int(request.json['usr_id'])))

@attendance.route('/create_attendance', methods=['POST'])
@cross_origin()
def create_attendance():
    return (model.create_attendance(request.files['file'], json.loads(request.form.get('data'))))

@attendance.route('/attendances', methods=['GET'])
@cross_origin()
def attendances():
    return jsonify(model.attendances())

@attendance.route('/update_attendance', methods=['PUT'])
@cross_origin()
def update_attendance():
    return (model.update_attendance(request.json["att_id"], request.json["att_val"]), request.json['att_date'])
   

@attendance.route('/delete_attendance', methods=['DELETE'])
@cross_origin()
def delete_attendance():
    return (model.delete_attendance(request.json["att_id"]))

@attendance.route('/select_attendance', methods=['GET'])
@cross_origin()
def select_attendance():
    return (model.select_attendance(request.json['att_id']))

