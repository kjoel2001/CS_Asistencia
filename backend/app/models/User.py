from app import db, ma
from .UserType import *

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

    def __init__(self, usr_dni, usr_pass, usr_photo, usr_name, usr_last_name, usr_dob, usr_email, usr_vec, ust_id):
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

