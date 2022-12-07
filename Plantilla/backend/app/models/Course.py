from app import db, ma

class Course(db.Model):
    cur_id   = db.Column(db.Integer, primary_key=True)
    cur_name = db.Column(db.String(70), unique=False)
    cur_des  = db.Column(db.String(100))

    def __init__(self, cur_name=None, cur_des=None):
        self.cur_name = cur_name
        self.cur_des  = cur_des

    def create_course(self, cur_name, cur_des):
        new_course = Course(cur_name,cur_des)
        db.session.add(new_course)
        db.session.commit()
        return course_schema.jsonify(new_course)

    def courses(self):
        all_courses = Course.query.all()
        result = courses_schema.dump(all_courses)
        return result

    def select_course(self, cur_id):
        course = Course.query.get(cur_id)
        return course_schema.jsonify(course)

    def update_course(self, cur_id, cur_name, cur_des):
        course = Course.query.get(cur_id)
        course.cur_name = cur_name
        course.cur_des = cur_des
        db.session.commit()
        return course_schema.jsonify(course)

    def delete_course(self, cur_id):
        course = Course.query.get(cur_id)
        db.session.delete(course)
        db.session.commit()
        return course_schema.jsonify(course)

class CourseSchema(ma.Schema):
    class Meta:
        fields = (
            'cur_id', 
            'cur_name', 
            'cur_des'
            )


course_schema  = CourseSchema()
courses_schema = CourseSchema(many=True)


