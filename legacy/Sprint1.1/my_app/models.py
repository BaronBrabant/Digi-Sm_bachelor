from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from my_app import app

pokerPlanningList = [1,2,3,5,8,13,21,34,55,89]

db = SQLAlchemy(app)
app.app_context().push()


"""
Description:
    The Task class is used to create a User story object which contains various information about the tasks
    contained within a sprint. This can be used as a backlog for a sprint but is though of as way to
    obtain a general overview of the tasks that need to be completed within a sprint.
"""
class Task(UserMixin, db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.String(128), nullable=False)  
    creation = db.Column(db.String(64), nullable=False)
    #for status 0 is to do, 1 is doing, 2 is done
    status = db.Column(db.Integer, nullable=False)
    pokerScore = db.Column(db.Integer, nullable=False)
    sprint_id = db.Column(db.Integer, db.ForeignKey('sprint.id'), nullable=True)
    sprint = db.relationship('Sprint', backref=db.backref('tasks', lazy=True))
    #the tasks wont be reassigned per projects so a simple integer is sufficient
    project_id = db.Column(db.Integer, nullable=False)


"""
Description:
    The Sprint class is used to create a new sprint object which is itself contained within a project
    through its foreign key.
    This allows for the creation of mutliple sprints per project.
"""
class Sprint(UserMixin, db.Model):
    __tablename__ = 'sprint'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creation = db.Column(db.String(64), nullable=False)
    #for status 0 is past sprint, 1 is current, 2 is future sprint
    status = db.Column(db.Boolean , nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    project = db.relationship('Project', backref=db.backref('sprint', lazy=True))


#many to many for users and projects as they can work on multiple projects 
#at once or they can have a list of old finished projects. 
#Meaning many users can work on many projects

"""
Description:
    This is an association table that is used to create a many to many relationship between the User and Project classes
    allowing for a user to be assigned to multiple projects and a project to have multiple users assigned to it.
"""
association_user_project = db.Table(
    "association_user_project",
    db.metadata,
    db.Column("user_id", db.ForeignKey("user.id"), primary_key=True),
    db.Column("project_id", db.ForeignKey("project.id"), primary_key=True),
)

"""
Description:
    The Project class is contains general information about the project.
"""
class Project(UserMixin, db.Model):
    __tablename__ = 'project'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.String(128), nullable=False)  
    creation = db.Column(db.String(64), nullable=False)
    #for status true is ongoing, false is finished
    status = db.Column(db.Boolean, nullable=False)
    #total score of finished tasks in project removed as can be calculated
    #backburnScore = db.Column(db.Integer, nullable=False)
    user = db.relationship("User", secondary = association_user_project, back_populates="project")


# OK
"""
Description:
    The user class allows for a new user to be registered to the system and to log him back in subsequently.
"""
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    passwd_hash = db.Column(db.String(128))
    name = db.Column(db.String(64), nullable=False)    
    firstname = db.Column(db.String(64), nullable=False)
    blocked = db.Column(db.Boolean, nullable=False)
    group = db.Column(db.Boolean, nullable=False)
    project = db.relationship("Project", secondary = association_user_project, back_populates="user")
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

"""
Description:
    This is a function to load some dummy data into the database to test the functionality of the application on startup.
"""
def createUserTaskInit():
# date pas sûre


    project1 = Project( 
                        name = "test project",
                        description = "This is the p",
                        creation = datetime.strptime('06/06/1999', '%d/%m/%Y').date(),
                        status = True
                      )

    project2 = Project( 
                        name = "test project 2",
                        description = "This doesnt work yet as there are no sprints or tasks implemented by default to prevent noneType error yet",
                        creation = datetime.strptime('06/06/1999', '%d/%m/%Y').date(),
                        status = False
                      )


    user1 = User(
                 username='admin123', 
                 name='henri', 
                 firstname='henri',
                 passwd_hash=generate_password_hash('admin123##!wqeq'), 
                 blocked=False, 
                 group=True
                )
    
    user2 = User(
                 username='worker123', 
                 name='henry', 
                 firstname='henry',
                 passwd_hash=generate_password_hash('admin123##!wqeq'), 
                 blocked=False, 
                 group=True
                )

    project1.user.append(user1)
    project1.user.append(user2)
    db.session.add(project1)
    project2.user.append(user1)
    db.session.add(project2)
    db.session.commit()

    sprint1 = Sprint(
                    creation = datetime.strptime('06/06/1999', '%d/%m/%Y').date(),
                    status = 1,
                    project_id = 1
                    )

    sprint2 = Sprint(
                    creation = datetime.strptime('06/06/1999', '%d/%m/%Y').date(),
                    status = 0,
                    project_id = 1
                    )

    db.session.add(sprint1)
    db.session.add(sprint2)

    for i in range(20):
        if i%3 == 0:
            task = Task(name="test"+str(i), description = "test %d"%i, creation = datetime.strptime('06/06/1999', '%d/%m/%Y').date(), status = 0, pokerScore = 1, sprint_id = 1, project_id  = 1)
        elif i%3 == 1:
            task = Task(name="test"+str(i), description = "test %d"%i, creation = datetime.strptime('06/06/1999', '%d/%m/%Y').date(), status = 0, pokerScore = 1, project_id  = 1)
        else:
            task = Task(name="test"+str(i), description = "test %d"%i, creation = datetime.strptime('06/06/1999', '%d/%m/%Y').date(), status = 0, pokerScore = 1, sprint_id = 2, project_id  = 1)
        
        db.session.add(task)

    db.session.commit()


"""
Description:
    This is a function to facilitate the creation of a new user in the rest of the code.
"""
def createUser(username, name, firstname, password, blocked = False, group = False):
# date pas sûre
    user1 = User(username=username, name=name, firstname=firstname,
            passwd_hash=password, blocked=False, group=False)

    return user1
