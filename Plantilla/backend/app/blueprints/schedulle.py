from flask import Blueprint, request, jsonify
from app.models.Schedulle import *
from flask_cors import cross_origin

schedulle = Blueprint('schedulle', __name__, url_prefix='/schedulle')
model = Schedulle()

@schedulle.route('/create_schedulle', methods=['POST'])
@cross_origin()
def create_schedulle():
    return (model.create_schedulle(request.json['gru_id'],
                                          request.json['sch_begin'], 
                                          request.json['sch_end'], 
                                          request.json['sch_day']))

@schedulle.route('/schedulles', methods=['GET'])
@cross_origin()
def schedulles():
    return jsonify(model.schedulles())

@schedulle.route('/update_schedulle', methods=['POST'])
@cross_origin()
def update_schedulle():
    return (model.update_schedulle(request.json['sch_id'],
                                   request.json['sch_begin'], 
                                   request.json['sch_end'], 
                                   request.json['sch_day']))

@schedulle.route('/delete_schedulle', methods=['POST'])
@cross_origin()
def delete_schedulle():
    return (model.delete_schedulle(request.json['sch_id']))

@schedulle.route('/select_schedulle', methods=['GET'])
@cross_origin()
def select_schedulle():
    return (request.json['sch_id'])

