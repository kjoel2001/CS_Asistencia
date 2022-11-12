from app import db, ma 
from .Group import Group
from .Student import Student

class Participation(db.Model):
    __tablename__ = 'participation'

    par_id   = db.Column(db.Integer, primary_key=True)
    par_date = db.Column(db.Integer)
    par_val  = db.Column(db.Integer)

    gru_id   = db.Column(db.Integer, db.ForeignKey(Group.gru_id))
    std_id   = db.Column(db.Integer, db.ForeignKey(Student.std_id))
    

class ParticipationSchema(ma.Schema):
    class Model:
        fields = (
            'par_id',
            'par_date',
            'par_val',
            'gru_id',
            'std_id'
        )

participation_schema  = ParticipationSchema()
participations_schema = ParticipationSchema(many=True)