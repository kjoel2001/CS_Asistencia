""" 
Table User  {
  usr_id    int [pk, increment] // auto-increment
  usr_dni  varchar
  usr_pass  timestamp
  usr_photo  int
  usr_name varchar
  usr_last_name varchar
  usr_dob   date
  usr_email varchar
  ust_id    int
} """

from crypt import methods
from flask import jsonify
from run import app, db, ma
import datetime
from flask import request

class User(db.Model):
    usr_id        = db.Column(db.Integer, primary_key=True)
    usr_dni       = db.Column(db.String(8), unique=True)
    usr_pass      = db.Column(db.Date)
    usr_photo     = db.Column(db.Integer)
    usr_name      = db.Column(db.String(20))
    usr_last_name = db.Column(db.String(20))
    usr_dob       = db.Column(db.DateTime())
    usr_email     = db.Column(db.String(30), unique=True)

    ust_id        = db.Column(db.Integer, db.ForeignKey('User_type.ust_id'))

    def __init__(self, usr_dni, usr_name, usr_last_name, usr_email, ust_id):
        self.usr_dni       = usr_dni
        self.usr_pass      = datetime.date.today()
        self.usr_name      = usr_name
        self.usr_last_name = usr_last_name
        self.usr_dob       = datetime.datetime.now()
        self.usr_email     = usr_email
        self.ust_id        = ust_id

db.create_all()

class UserSchema(ma.Schema):
    class Meta:
        fields = (
            'usr_dni', 
            'usr_pass',
            'usr_name', 
            'usr_last_name',
            'usr_dob',
            'usr_email',
            'ust_id'
            )

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route('/create_user', methods=['POST'])
def create_user():
    print(request.json)

    usr_dni  = request.json['usr_dni']
    usr_name = request.json['usr_name']
    usr_last_name = request.json['usr_last_name']
    usr_email = request.json['usr_email']
    ust_id = request.json['ust_id']

    new_user = User(usr_dni, usr_name, usr_last_name, usr_email, ust_id)
    
    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

@app.route('/users', methods=['POST'])
def users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)

@app.route('/delete_user/<usr_id>', methods=['POST'])
def delete_user(usr_id):
    user = User.query.get(usr_id)

    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)

