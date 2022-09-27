""" Table User_type {
  ust_id int [pk, increment]
  ust_name varchar
 } """

from run import app, db, ma
from flask import request, jsonify

# table user_type
class User_type(db.Model):
    ust_id   = db.Column(db.Integer, primary_key=True)
    ust_name = db.Column(db.String(20), unique=False)

    def __init__(self, ust_name):
        self.ust_name = ust_name

db.create_all()

class UserTypeSchema(ma.Schema):
    class Meta:
        fields = ('ust_id', 'ust_name')

user_type_schema  = UserTypeSchema()
users_type_schema = UserTypeSchema(many=True)

@app.route('/create_user_type', methods=['POST'])
def create_user_type():
    print(request.json)

    ust_name = request.json['ust_name']

    new_usertype = User_type(ust_name)
    
    db.session.add(new_usertype)
    db.session.commit()

    return user_type_schema.jsonify(new_usertype)

@app.route('/users_type', methods=['POST'])
def users_type():
    all_users_type = User_type.query.all()
    result = users_type_schema.dump(all_users_type)

    return jsonify(result)

@app.route('/update_user_type/<ust_id>', methods=['POST'])
def update_user_type(ust_id):
    user_type = User_type.query.get(ust_id)
    name = request.json['ust_name']

    user_type.ust_name = name
    
    db.session.commit()
    return user_type_schema.jsonify(user_type)

@app.route('/delete_user_type/<id>', methods=['POST'])
def delete_user_type(ust_id):
    user_type = User_type.query.get(ust_id)
    
    db.session.delete(user_type)
    db.session.commit()

    return user_type_schema.jsonify(user_type)