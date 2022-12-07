from flask import request, jsonify
from app import db, ma

class User_type(db.Model):
    __tablename__ = 'user_type'

    ust_id   = db.Column(db.Integer, primary_key=True)
    ust_name = db.Column(db.String(20), unique=False)

    def __init__(self, ust_name=None):
        self.ust_name = ust_name

    def __repr__(self) -> str:
        return f"User type (ID={self.ust_id!r}, name={self.ust_name!r})"

    def create_user_type(self, ust_name):
        new_usertype = User_type(ust_name)
        db.session.add(new_usertype)
        db.session.commit()
        return user_type_schema.jsonify(new_usertype)

    def users_type(self):
        all_users_type = User_type.query.all()
        result = users_type_schema.dump(all_users_type)
        return result

    def update_user_type(self, ust_id, ust_name):
        user_type = User_type.query.get(ust_id)

        user_type.ust_name = ust_name

        db.session.commit()
        return user_type_schema.jsonify(user_type)

    def delete_user_type(self, ust_id):
        user_type = User_type.query.get(ust_id)
    
        db.session.delete(user_type)
        db.session.commit()

        return user_type_schema.jsonify(user_type)

    def select_user_type(self, ust_id):
        user_type = User_type.query.get(ust_id) 

        return user_type_schema.jsonify(user_type)

class UserTypeSchema(ma.Schema):
    class Meta:
        fields = ('ust_id', 'ust_name')

user_type_schema  = UserTypeSchema()
users_type_schema = UserTypeSchema(many=True)



