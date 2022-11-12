from app import db, ma

class Course(db.Model):
    cur_id   = db.Column(db.Integer, primary_key=True)
    cur_name = db.Column(db.String(70), unique=False)
    cur_des  = db.Column(db.String(100))

    def __init__(self, cur_name, cur_des):
        self.cur_name = cur_name
        self.cur_des  = cur_des


class CourseSchema(ma.Schema):
    class Meta:
        fields = (
            'cur_id', 
            'cur_name', 
            'cur_des'
            )


course_schema  = CourseSchema()
courses_schema = CourseSchema(many=True)


