""" Table Teacher {
  tea_id int [pk, increment]
  usr_id int
  tea_type varchar //tp, tc, research
  tea_cat varchar // contratado o nombrado
} """

from urllib import request
from run import app, db, ma

class Teacher(db.Model):
    tea_id   = db.Column(db.Integer, primary_key=True)
    tea_cat  = db.Column(db.String(10))
    tea_type = db.Column(db.String(8))

    usr_id = db.Column(db.Integer, db.ForeingKey('User.usr_id'))

    def __init__(self, tea_id, tea_cat, tea_type, usr_id):
        self.tea_id   = tea_id
        self.tea_cat  = tea_cat
        self.tea_type = tea_type

        self.usr_id   = usr_id

db.create_all()

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

@app.route('/create_teacher', methods=['POST'])
def create_teacher():
    print(request.json)

    tea_id = request.json['tea_id']
    tea_cat = request.json['tea_cat']
    tea_type = request.json['tea_type']
    usr_id = request.json['usr_id']

    new_teacher = Teacher(tea_id, tea_cat, tea_type, usr_id)

    db.session.add(new_teacher)
    db.session.commit()

    return teacher_schema.jsonify(new_teacher)

@app.route('/teachers', methods=['POST'])
def teachers():
    all_teachers = Teacher.query.all()
    result = teachers_schema.dump(all_teachers)

    return jsonify(result)

@app.route('/update_teacher/<tea_id>')
def update_teacher(tea_id):
    teacher = Teacher.query.get(tea_id)
    tea_cat = request.json['tea_cat']
    tea_type = request.json['tea_type']

    teacher.tea_cat = tea_cat
    teacher.tea_type = tea_type

    db.session.commit()

    return teacher_schema.jsonify(teacher)
