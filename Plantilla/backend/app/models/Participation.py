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
    
    def __init__(self, par_date=None, par_val=None, gru_id=None, std_id=None):
        self.par_date = par_date
        self.par_val  = par_val
        self.gru_id   = gru_id
        self.std_id   = std_id

    def create_participation(self, par_date, par_val, gru_id, std_id):
        new_participation = Participation(par_date, par_val, gru_id, std_id)
        db.session.add(new_participation)
        db.session.commit()
        return participation_schema.jsonify(new_participation)

    def participations(self):
        all_participations = Participation.query.all()
        result = participations_schema.dump(all_participations)
        return result

    def update_participation(self,par_id, par_date, par_val):
        participation = Participation.query.get(par_id)
        participation.par_date = par_date
        participation.par_val = par_val
        db.session.commit()
        return participation_schema.jsonify(participation)

    def delete_participation(self,par_id):
        participation = Participation.query.get(par_id)
        db.session.delete(participation)
        db.session.commit()
        return participation_schema.jsonify(participation)

    def select_participation(self, std_id):
        participation = Participation.query.get(std_id) 
        return participation_schema.jsonify(participation)


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