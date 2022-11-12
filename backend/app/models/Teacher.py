from app import db, ma
from .User import User

class Teacher(db.Model):
    __tablename__ = 'teacher'
    
    tea_id   = db.Column(db.Integer, primary_key=True)
    tea_cat  = db.Column(db.String(10))
    tea_type = db.Column(db.String(8))

    usr_id = db.Column(db.Integer, db.ForeignKey(User.usr_id))

    def __init__(self, tea_cat, tea_type, usr_id):
        self.tea_cat  = tea_cat
        self.tea_type = tea_type

        self.usr_id   = usr_id

class TeacherSchema(ma.Schema):
    class Meta:
        fields = (
            'tea_id', 
            'tea_cat', 
            'tea_type', 
            'usr_id'
            )

teacher_schema = TeacherSchema()
teachers_schema = TeacherSchema(many=True)