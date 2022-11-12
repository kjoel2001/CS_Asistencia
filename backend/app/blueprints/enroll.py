from flask import Blueprint, request, jsonify
from app.models.Enroll import *
from flask_cors import cross_origin

enroll = Blueprint('enroll', __name__, url_prefix='/enroll')

@enroll.route('/create_enroll', methods=['POST'])
@cross_origin()
def create_enroll():
    print(request.json)
    
    enr_date = request.json['enr_date']
    std_id   = request.json['std_id']
    gru_id   = request.json['gru_id']

    new_enroll = Enroll(enr_date, std_id, gru_id)
    db.session.add(new_enroll)
    db.session.commit()

    return enroll_schema.jsonify(new_enroll)

@enroll.route('/enrolls', methods=['POST'])
@cross_origin()
def enrolls():
    all_enrolls = enroll.query.all()
    result = enrolls_schema.dump(all_enrolls)
    return jsonify(result)

@enroll.route('/update_enroll/<int:enr_id>', methods=['POST'])
@cross_origin()
def update_enroll(enr_id):
    enroll = enroll.query.get(enr_id)
    
    enr_date = request.json['tea_cat']
    gru_id = request.json['gru_id']

    enroll.enr_date = enr_date
    enroll.gru_id = gru_id
    
    db.session.commit()
    return enroll_schema.jsonify(enroll)

@enroll.route('/delete_enroll/<int:enr_id>', methods=['POST'])
@cross_origin()
def delete_enroll(enr_id):
    enroll = enroll.query.get(enr_id)
    
    db.session.delete(enroll)
    db.session.commit()

    return enroll_schema.jsonify(enroll)

@enroll.route('/select_enroll/<int:enr_id>', methods=['POST'])
@cross_origin()
def select_enroll(enr_id):
    enroll = enroll.query.get(enr_id) 

    return enroll_schema.jsonify(enroll)

