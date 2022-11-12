from flask import Blueprint, request, jsonify
from app.models.Schedulle import *
from flask_cors import cross_origin

schedulle = Blueprint('schedulle', __name__, url_prefix='/schedulle')


@schedulle.route('/create_schedulle', methods=['POST'])
@cross_origin()
def create_schedulle():
    print(request.json)
    
    sch_begin = request.json['sch_begin']
    sch_end   = request.json['sch_end']
    sch_day   = request.json['sch_day']
    gru_id    = request.json['gru_id']

    new_schedulle = schedulle(sch_begin, sch_end, sch_day, gru_id)
    db.session.add(new_schedulle)
    db.session.commit()
    return schedulle_schema.jsonify(new_schedulle)


@schedulle.route('/schedulles', methods=['POST'])
@cross_origin()
def schedulles():
    all_schedulles = schedulle.query.all()
    result = schedulles_schema.dump(all_schedulles)
    return jsonify(result)

@schedulle.route('/update_schedulle/<int:sch_id>', methods=['POST'])
@cross_origin()
def update_schedulle(sch_id):
    schedulle = schedulle.query.get(sch_id)
    
    sch_begin = request.json['sch_begin']
    sch_end = request.json['sch_end']
    sch_day = request.json['sch_day']

    schedulle.sch_begin = sch_begin
    schedulle.sch_end   = sch_end
    schedulle.sch_day   = sch_day

    db.session.commit()
    return schedulle_schema.jsonify(schedulle)


@schedulle.route('/delete_schedulle/<int:sch_id>', methods=['POST'])
@cross_origin()
def delete_schedulle(sch_id):
    schedulle = schedulle.query.get(sch_id)
    
    db.session.delete(schedulle)
    db.session.commit()
    return schedulle_schema.jsonify(schedulle)


@schedulle.route('/select_schedulle/<int:sch_id>', methods=['POST'])
@cross_origin()
def select_schedulle(sch_id):
    schedulle = schedulle.query.get(sch_id) 

    return schedulle_schema.jsonify(schedulle)

