from .Teacher import Teacher
from .Course import Course
from app import db, ma

class Group(db.Model):
    __tablename__ = 'group'
    
    gru_id   = db.Column(db.Integer, primary_key=True)
    gru_name = db.Column(db.String(20))
    
    cur_id   = db.Column(db.Integer, db.ForeignKey(Course.cur_id))
    tea_id   = db.Column(db.Integer, db.ForeignKey(Teacher.tea_id))

    def __init__(self, gru_name, cur_id, tea_id):
        self.gru_name = gru_name
        self.cur_id   = cur_id
        self.tea_id   = tea_id

class GroupSchema(ma.Schema):
    class Meta:
        fields = (
            'gru_id',
            'gru_name',
            'cur_id',
            'tea_id'
        )

group_schema  = GroupSchema()
groups_schema = GroupSchema(many=True)