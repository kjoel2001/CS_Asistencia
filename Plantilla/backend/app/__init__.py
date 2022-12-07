from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_session import Session
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:12345678@127.0.0.1:5432/asistencia"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # par q no de warnings
app.config['SECRET_KEY'] = "SECRET"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)
jwt = JWTManager(app)

db  = SQLAlchemy(app)
ma  = Marshmallow(app)

from .models import User
from .models import UserType
from .models import Teacher
from .models import Student
from .models import Group
from .models import Course
from .models import Attendance
from .models import Schedulle
from .models import Participation
from .models import Enroll

db.create_all()

from app.blueprints.usertype import usertype
from app.blueprints.user import user
from app.blueprints.attendance import attendance
from app.blueprints.couse import course
from app.blueprints.student import student
from app.blueprints.teacher import teacher
from app.blueprints.group import group
from app.blueprints.enroll import enroll
from app.routes.auth import routes_auth
from app.auth.token import login_web_token
from app.blueprints.schedulle import schedulle
from app.blueprints.participation import participation
from flask_cors import CORS

app.register_blueprint(usertype)
app.register_blueprint(user)
app.register_blueprint(course)
app.register_blueprint(student)
app.register_blueprint(teacher)
app.register_blueprint(group)
app.register_blueprint(enroll)
app.register_blueprint(attendance)
app.register_blueprint(routes_auth)
app.register_blueprint(login_web_token)
app.register_blueprint(schedulle)
app.register_blueprint(participation)
CORS(app)

def create_app():
    return app

if __name__ == '__main__':
    app.run(debug=True)