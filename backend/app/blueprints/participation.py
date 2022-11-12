from flask import Blueprint, request, jsonify
from app.models.Participation import *
from flask_cors import cross_origin

participation = Blueprint('participation', __name__, url_prefix='/participation')


@participation.route('/create_participation', methods=['POST'])
@cross_origin()
def create_participation():
    print(request.json)
    
    par_date = request.json['gro_name']
    par_val  = request.json['cur_id']
    std_id   = request.json['std_id']
    std_id   = request.json['std_id']

    new_participation = participation(par_date, par_val, std_id, std_id)
    db.session.add(new_participation)
    db.session.commit()
    return participation_schema.jsonify(new_participation)


@participation.route('/participations', methods=['POST'])
@cross_origin()
def participations():
    all_participations = participation.query.all()
    result = participations_schema.dump(all_participations)
    return jsonify(result)

@participation.route('/update_participation/<int:std_id>', methods=['POST'])
@cross_origin()
def update_participation(std_id):
    participation = participation.query.get(std_id)
    
    par_val = request.json['par_val']

    participation.par_val = par_val
    db.session.commit()
    return participation_schema.jsonify(participation)


@participation.route('/delete_participation/<int:att_id>', methods=['POST'])
@cross_origin()
def delete_participation(att_id):
    participation = participation.query.get(att_id)
    
    db.session.delete(participation)
    db.session.commit()

    return participation_schema.jsonify(participation)

@participation.route('/select_participation/<int:std_id>', methods=['POST'])
@cross_origin()
def select_participation(std_id):
    participation = participation.query.get(std_id) 

    return participation_schema.jsonify(participation)

