from numpy import std
from .Student import Student
from .Group import Group
from app import db, ma


class Enroll(db.Model):
    __tablename__ = 'enroll' 

    enr_id   = db.Column(db.Integer, primary_key=True)
    enr_date = db.Column(db.Date())

    std_id   = db.Column(db.Integer, db.ForeignKey(Student.std_id))
    gru_id   = db.Column(db.Integer, db.ForeignKey(Group.gru_id))

    def __init__(self, enr_date, std_id, gru_id):
        self.enr_date = enr_date
        self.std_id   = std_id
        self.gru_id   = gru_id

class EnrollSchema(ma.Schema):
    class Meta:
        fields = (
            'end_id',
            'enr_date',
            'std_id',
            'gru_id'
        )

enroll_schema  = EnrollSchema()
enrolls_schema = EnrollSchema(many=True)