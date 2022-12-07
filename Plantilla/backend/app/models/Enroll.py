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

    def __init__(self, enr_date=None, std_id=None, gru_id=None):
        self.enr_date = enr_date
        self.std_id   = std_id
        self.gru_id   = gru_id

    def create_enroll(self, enr_date, std_id, gru_id):
        new_enroll = Enroll(enr_date, std_id, gru_id)
        db.session.add(new_enroll)
        db.session.commit()
        return enroll_schema.jsonify(new_enroll)

    def enrolls(self):
        all_enrolls = Enroll.query.all()
        result = enrolls_schema.dump(all_enrolls)
        return result

    def update_enroll(self, enr_id, enr_date, gru_id):
        enroll = Enroll.query.get(enr_id)
        enroll.enr_date = enr_date
        enroll.gru_id = gru_id
        db.session.commit()
        return enroll_schema.jsonify(enroll)

    def delete_enroll(self, enr_id):
        enroll = Enroll.query.get(enr_id)    
        db.session.delete(enroll)
        db.session.commit()
        return enroll_schema.jsonify(enroll)

    def select_enroll(self, enr_id):
        enroll = Enroll.query.get(enr_id) 
        return enroll_schema.jsonify(enroll)



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