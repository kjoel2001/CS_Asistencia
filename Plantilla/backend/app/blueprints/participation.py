from flask import Blueprint, request, jsonify
from app.models.Participation import *
from flask_cors import cross_origin

participation = Blueprint('participation', __name__, url_prefix='/participation')
model = Participation()

@participation.route('/create_participation', methods=['POST'])
@cross_origin()
def create_participation():
    return (model.create_participation(request.json['par_date'],
                                       request.json['par_val'],
                                       request.json['gru_id'],
                                       request.json['std_id']))
                                       
    
@participation.route('/participations', methods=['GET'])
@cross_origin()
def participations():
    return jsonify(model.participations())

@participation.route('/update_participation', methods=['POST'])
@cross_origin()
def update_participation():
    return (model.update_participation(request.json['par_id'], 
                                       request.json['par_date'],
                                       request.json['par_val'],))

@participation.route('/delete_participation', methods=['POST'])
@cross_origin()
def delete_participation():
    return (model.delete_participation(request.json['par_id']))

@participation.route('/select_participation', methods=['GET'])
@cross_origin()
def select_participation():
    return (model.select_participation(request.json['par_id']))

