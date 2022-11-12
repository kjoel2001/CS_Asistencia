from app import db, ma
from .Group import Group
from .Student import Student

class Attendance(db.Model):
    __tablename__ = 'attendance' 
    
    att_id    = db.Column(db.Integer, primary_key=True)
    att_val   = db.Column(db.Boolean)
    att_date  = db.Column(db.Integer)
 
    gru_id    = db.Column(db.Integer, db.ForeignKey(Group.gru_id))
    std_id    = db.Column(db.Integer, db.ForeignKey(Student.std_id))
    
    def __init__(self, att_val, att_date, gru_id, std_id):
        self.att_val  = att_val
        self.att_date = att_date
        self.gru_id   = gru_id
        self.std_id   = std_id

class AttendanceSchema(ma.Schema):
    class Meta:
        fields = (
            'att_id',
            'att_val',
            'att_date',
            'gru_id',
            'std_id'
        )

attendance_schema  = AttendanceSchema()
attendances_schema = AttendanceSchema(many=True)