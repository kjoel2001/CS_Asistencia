from app import db, ma
from .User import User

class Teacher(db.Model):
    __tablename__ = 'teacher'
    
    tea_id   = db.Column(db.Integer, primary_key=True)
    tea_cat  = db.Column(db.String(10))
    tea_type = db.Column(db.String(8))

    usr_id = db.Column(db.Integer, db.ForeignKey(User.usr_id))

    def __init__(self, tea_cat=None, tea_type=None, usr_id=None):
        self.tea_cat  = tea_cat
        self.tea_type = tea_type
        self.usr_id   = usr_id

    def create_teacher(self, usr_id, tea_type, tea_cat):
        new_teacher = Teacher(tea_cat, tea_type, usr_id)
        db.session.add(new_teacher)
        db.session.commit()
        return teacher_schema.jsonify(new_teacher)

    def teachers(self):
        all_teachers = Teacher.query.all()
        result = teachers_schema.dump(all_teachers)
        return result

    def update_teacher(self, tea_id, tea_cat, tea_type):
        teacher = Teacher.query.get(tea_id)

        teacher.tea_cat = tea_cat
        teacher.tea_type = tea_type

        db.session.commit()
        return teacher_schema.jsonify(teacher)

    def delete_teacher(self, tea_id):
        teacher = Teacher.query.get(tea_id)
        db.session.delete(teacher)
        db.session.commit()

        return teacher_schema.jsonify(teacher)

    def select_teacher(self, tea_id):
        teacher = Teacher.query.get(tea_id) 
        return teacher_schema.jsonify(teacher)

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