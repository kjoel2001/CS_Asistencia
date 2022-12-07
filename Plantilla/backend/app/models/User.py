from app import db, ma
from .UserType import *
from app.blueprints.functions import *
from flask import request
import requests, json

class User(db.Model):
    __tablename__ = 'user'

    usr_id        = db.Column(db.Integer, primary_key=True)
    usr_dni       = db.Column(db.String(8), unique=True)
    usr_pass      = db.Column(db.String(20))
    usr_photo     = db.Column(db.Text) # direccion de la foto 
    usr_name      = db.Column(db.String(20))
    usr_last_name = db.Column(db.String(20))
    usr_dob       = db.Column(db.Date())
    usr_email     = db.Column(db.String(30), unique=True)
    usr_vec       = db.Column(db.Text) # vector resultado de la foto
    
    ust_id        = db.Column(db.Integer, db.ForeignKey(User_type.ust_id))

    def __init__(self, usr_dni=None, usr_pass=None, usr_photo=None, 
                usr_name=None, usr_last_name=None, usr_dob=None, 
                usr_email=None, usr_vec=None, ust_id=None):
        
        self.usr_dni       = usr_dni
        self.usr_pass      = usr_pass
        self.usr_photo     = usr_photo
        self.usr_name      = usr_name
        self.usr_last_name = usr_last_name
        self.usr_dob       = usr_dob
        self.usr_email     = usr_email
        self.usr_vec       = usr_vec

        self.ust_id        = ust_id

    def __repr__(self) -> str:
        return f"User(id={self.usr_id!r}, name={self.usr_name!r}, last name={self.usr_last_name!r})"

    def create_user(self, file, data={}):
        if request.method == 'POST':
            path = savePath(file)

            # call openfaceAPI, return vector de caracteristicas ##################################
            result = callOpenFaceAPI(path)

            usr_dni         = data['usr_dni']
            usr_photo       = path
            usr_pass        = data['usr_pass']
            usr_name        = data['usr_name']
            usr_last_name   = data['usr_last_name']
            usr_dob         = data['usr_dob']
            usr_email       = data['usr_email']
            usr_vec         = toString(result)
            ust_id          = data['ust_id']

            new_user = User(
                            usr_dni,  
                            usr_pass,
                            usr_photo,
                            usr_name,
                            usr_last_name, 
                            usr_dob, 
                            usr_email, 
                            usr_vec, 
                            ust_id
                            )

            db.session.add(new_user)
            db.session.commit()

        return user_schema.jsonify(new_user)

    def users(self):
        all_users = User.query.all()
        result = users_schema.dump(all_users)
        return result

    def delete_user(self, usr_id):
        user = User.query.get(usr_id)
        db.session.delete(user)
        db.session.commit()

        return user_schema.jsonify(user)

    def update_user(self, usr_id, usr_name):
        user = User.query.get(usr_id)
        user.usr_name = usr_name
        db.session.commit()
        return user_schema.jsonify(user)

    def select_user(self, usr_id):
        user = User.query.get(usr_id) 
        return user_schema.jsonify(user)

    def select_dni(self, usr_dni):
        user = User.query.filter_by(usr_dni=usr_dni).first_or_404()
        return user_schema.jsonify(user)

class UserSchema(ma.Schema):
    class Meta:
        fields = (
            'usr_id',
            'usr_dni', 
            'usr_photo',
            'usr_pass',
            'usr_name', 
            'usr_last_name',
            'usr_dob',
            'usr_email',
            'usr_vec',
            'ust_id'
            )

user_schema = UserSchema()
users_schema = UserSchema(many=True)

