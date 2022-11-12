from flask import request, jsonify
from app import db, ma

class User_type(db.Model):
    __tablename__ = 'user_type'

    ust_id   = db.Column(db.Integer, primary_key=True)
    ust_name = db.Column(db.String(20), unique=False)

    def __init__(self, ust_name):
        self.ust_name = ust_name

    def __repr__(self) -> str:
        return f"User type (ID={self.ust_id!r}, name={self.ust_name!r})"

 
class UserTypeSchema(ma.Schema):
    class Meta:
        fields = ('ust_id', 'ust_name')

user_type_schema  = UserTypeSchema()
users_type_schema = UserTypeSchema(many=True)



