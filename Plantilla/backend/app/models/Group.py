from .Teacher import Teacher
from .Course import Course
from app import db, ma

class Group(db.Model):
    __tablename__ = 'group'
    
    gru_id   = db.Column(db.Integer, primary_key=True)
    gru_name = db.Column(db.String(20))
    
    cur_id   = db.Column(db.Integer, db.ForeignKey(Course.cur_id))
    tea_id   = db.Column(db.Integer, db.ForeignKey(Teacher.tea_id))

    def __init__(self, gru_name=None, cur_id=None, tea_id=None):
        self.gru_name = gru_name
        self.cur_id   = cur_id
        self.tea_id   = tea_id

    def create_group(self, gro_name, cur_id, tea_id):     
        new_group = Group(gro_name, cur_id, tea_id)
        db.session.add(new_group)
        db.session.commit()
        return group_schema.jsonify(new_group)

    def groups(self):
        all_groups = Group.query.all()
        result = groups_schema.dump(all_groups)
        return result

    def update_group(self, gru_id, gru_name, cur_id, tea_id):
        group = Group.query.get(gru_id)
        group.gru_name = gru_name
        group.tea_id = tea_id
        group.cur_id = cur_id
        db.session.commit()
        return group_schema.jsonify(group)

    def delete_group(self, gru_id):
        group = Group.query.get(gru_id)
        db.session.delete(group)
        db.session.commit()
        return group_schema.jsonify(group)


    def select_group(gru_id):
        group = Group.query.get(gru_id) 

        return group_schema.jsonify(group)



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