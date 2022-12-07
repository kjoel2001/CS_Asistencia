from app import db, ma
from .Group import Group

class Schedulle(db.Model):
    __tablename__ = 'schedulle'

    sch_id    = db.Column(db.Integer, primary_key=True)
    sch_begin = db.Column(db.Time)
    sch_end   = db.Column(db.Time)
    sch_day   = db.Column(db.String(20))

    gru_id    = db.Column(db.Integer, db.ForeignKey(Group.gru_id))

    def __init__(self, sch_begin=None, sch_end=None, sch_day=None, gru_id=None):
        self.sch_begin = sch_begin
        self.sch_end   = sch_end
        self.sch_day   = sch_day
        self.gru_id    = gru_id

    def create_schedulle(self, gru_id, sch_begin, sch_end, sch_day):
        new_schedulle = Schedulle(sch_begin, sch_end, sch_day, gru_id)
        db.session.add(new_schedulle)
        db.session.commit()
        return schedulle_schema.jsonify(new_schedulle)

    def schedulles(self):
        all_schedulles = Schedulle.query.all()
        result = schedulles_schema.dump(all_schedulles)
        return result

    def update_schedulle(self, sch_id, sch_begin, sch_end, sch_day):
        schedulle = Schedulle.query.get(sch_id)

        schedulle.sch_begin = sch_begin
        schedulle.sch_end   = sch_end
        schedulle.sch_day   = sch_day

        db.session.commit()
        return schedulle_schema.jsonify(schedulle)

    def delete_schedulle(self, sch_id):
        schedulle = Schedulle.query.get(sch_id)

        db.session.delete(schedulle)
        db.session.commit()
        return schedulle_schema.jsonify(schedulle)

    def select_schedulle(self, sch_id):
        schedulle = Schedulle.query.get(sch_id) 
        return schedulle_schema.jsonify(schedulle)

class SchedulleSchema(ma.Schema):
    class Meta:
        fields = (
            'sch_id',
            'sch_begin',
            'sch_end',
            'sch_day',
            'gru_id'
        )

schedulle_schema  = SchedulleSchema()
schedulles_schema = SchedulleSchema(many=True)