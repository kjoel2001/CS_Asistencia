from flask import Blueprint, request, jsonify
from app.models.Enroll import *
from flask_cors import cross_origin

enroll = Blueprint('enroll', __name__, url_prefix='/enroll')
model = Enroll()

@enroll.route('/create_enroll', methods=['POST'])
@cross_origin()
def create_enroll():
    return (model.create_enroll(request.json['end_date'],
                                request.json['std_id'], 
                                request.json['gru_id']))

@enroll.route('/enrolls', methods=['GET'])
@cross_origin()
def enrolls():
    return jsonify(model.enrolls())

@enroll.route('/update_enroll', methods=['PUT'])
@cross_origin()
def update_enroll():
    return (model.update_enroll(request.json['enr_id'],
                                       request.json['end_date'], 
                                       request.json['gru_id']))

@enroll.route('/delete_enroll', methods=['DELETE'])
@cross_origin()
def delete_enroll():
    return (model.delete_enroll(request.json['enr_id']))

@enroll.route('/select_enroll', methods=['GET'])
@cross_origin()
def select_enroll():
    return (model.select_enroll(request.json['end_id']))

