from app import db, ma
from .Group import Group

class Schedulle(db.Model):
    __tablename__ = 'schedulle'

    sch_id    = db.Column(db.Integer, primary_key=True)
    sch_begin = db.Column(db.Time)
    sch_end   = db.Column(db.Time)
    sch_day   = db.Column(db.String(20))

    gru_id    = db.Column(db.Integer, db.ForeignKey(Group.gru_id))

    def __init__(self, sch_begin, sch_end, sch_day, gru_id):
        self.sch_begin = sch_begin
        self.sch_end   = sch_end
        self.sch_day   = sch_day
        self.gru_id    = gru_id
        
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