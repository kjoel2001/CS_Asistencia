from app import db, ma
from .User import User

class Student(db.Model):
    __tablename__ = 'student'
    
    std_id      = db.Column(db.Integer, primary_key=True)
    std_regular = db.Column(db.Boolean)
    std_year    = db.Column(db.Date())

    usr_id = db.Column(db.Integer, db.ForeignKey(User.usr_id))

    def __init__(self, std_regular, std_year, usr_id):
        self.std_regular = std_regular
        self.std_year    = std_year
        self.usr_id      = usr_id

class StudentSchema(ma.Schema):
    class Meta:
        fields = (
            'std_id',
            'std_regular',
            'std_year',
            'usr_id'
        )

student_schema  = StudentSchema()
students_schema = StudentSchema(many=True)