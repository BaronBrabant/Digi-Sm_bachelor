from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from . import app

db = SQLAlchemy(app)
app.app_context().push()

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    passwd_hash = db.Column(db.String(128))
    name = db.Column(db.String(64), nullable=False)    
    firstname = db.Column(db.String(64), nullable=False)
    birthday = db.Column(db.String(64), nullable=False)
    #This will be to block access to emplyees no longer working on the project
    blocked = db.Column(db.Boolean, nullable=False)
    #This will be team-member, team-leader/scrum organiser
    group = db.Column(db.Boolean, nullable=False)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)


class Task(UserMixin, db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.String(128), nullable=False)  
    due = db.Column(db.String(64), nullable=False)
    done = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('tasks', lazy=True))

def createUser(username, name, firstname, birthday, password, blocked = False, group = False):
# date pas sûre
    user1 = User(username=username, name=name, firstname=firstname,
            birthday=datetime.strptime("%s"%birthday, '%d/%m/%Y').date(),
            passwd_hash=password, blocked=False, group=False)

    return user1

def createUserInit():
# date pas sûre
    user1 = User(username='admin123', name='henri', firstname='henri',
            birthday=datetime.strptime('06/06/1999', '%d/%m/%Y').date(),
            passwd_hash=generate_password_hash('admin123'), blocked=False, group=True)


    db.session.add(user1)
    db.session.commit()