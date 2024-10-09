from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from my_app import app
import random

pokerPlanningList = [0, 0.5, 1,2,3,5,8,13,21,34,55,89]

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
    name = db.Column(db.String(64), unique=False, nullable=False)
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

"""
Description:
    This contains the order of the tasks/Userstories in the table in order to
    make the drag and drop feature persistent.    
"""

class TaskSprintOrder(UserMixin, db.Model):
    __tablename__ = 'task_sprint_order'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    sprint_id = db.Column(db.Integer, db.ForeignKey('sprint.id'), nullable=False)
    order = db.Column(db.Integer, nullable=False)

"""
Description:
    This is a table which serves as a request table for a user to be able receive and accept or decline a project request.
    The user can then be added to the project through the data in this table.
    The user can also decline the request which will simply delete the row.
    Furthermore the friendslist association below serves as a quick table to find past users but a request can be sent only with the username of the user too.
"""

class ProjectRequest(UserMixin, db.Model):
    __tablename__ = 'project_request'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    

class FriendRequest(UserMixin, db.Model):
    __tablename__ = 'friend_request'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    friend_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class FriendsList(UserMixin, db.Model):
    __tablename__ = 'friends_list'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    friend_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #still hesitating on whether to use a backref of not but i dont need to access project request from user or project

"""
association_user_friend = db.Table(
    "association_user_friend",
    db.metadata,
    db.Column("user_id", db.ForeignKey("user.id"), primary_key=True),
    db.Column("friend_id", db.ForeignKey("user.id"), primary_key=True),
)
"""

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
    name = db.Column(db.String(64), unique=False, nullable=False)
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
    #true is an admin, false is a normal user
    group = db.Column(db.Boolean, nullable=False)
    project = db.relationship("Project", secondary = association_user_project, back_populates="user")
    
    def set_password(self, passwd):
        self.passwd_hash = generate_password_hash(passwd)
    
    def check_password(self, passwd):
        return check_password_hash(self.passwd_hash, passwd)


"""
Description:
    This is a function to load some dummy data into the database to test the functionality of the application on startup.
"""
def createUserTaskInit():
# date pas sûre


    project1 = Project( 
                        name = "test project",
                        description = "This is the test project filled with the user stories and sprits used to develop this website",
                        creation = datetime.strptime('06/05/2022', '%d/%m/%Y').date(),
                        status = True
                      )

    project2 = Project( 
                        name = "test project 2",
                        description = "Empty example project",
                        creation = datetime.strptime('06/03/2022', '%d/%m/%Y').date(),
                        status = False
                      )


    user1 = User(
                 username='admin123', 
                 name='Ken', 
                 firstname='Thompson',
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
                 group=False
                )
    
    user3 = User(
                 username='lonelyWorkerTest', 
                 name='henry', 
                 firstname='henry',
                 passwd_hash=generate_password_hash('admin123##!wqeq'), 
                 blocked=False, 
                 group=False
                )
    
    
    
    

    project1.user.append(user1)
    project1.user.append(user2)
    db.session.add(project1)
    project2.user.append(user1)
    project2.user.append(user3)
    db.session.add(project2)
    db.session.commit()
    db.session.add(user3)



    sprint1 = Sprint(
                    creation = datetime.strptime('06/06/2022', '%d/%m/%Y').date(),
                    status = 1,
                    project_id = 1
                    )

    sprint2 = Sprint(
                    creation = datetime.strptime('06/08/2022', '%d/%m/%Y').date(),
                    status = 1,
                    project_id = 1
                    )
    
    sprint3 = Sprint(
                    creation = datetime.strptime('06/10/2022', '%d/%m/%Y').date(),
                    status = 0,
                    project_id = 1
                    )

    db.session.add(sprint1)
    db.session.add(sprint2)
    db.session.add(sprint3)

    exampleUserStory = ["As a team-member on the team I want to use it as a checklist, so that I can make sure my daily workflow is agile.",
                        "As a junior developer on the team I want a tool to learn, so that I can have hands-on experience while working.",
                        "As a team-member I would to be able to mark sprints or tasks as finished, so that I can track the advancement of the project",
                        "As a scrum creator I would like to be able to control things such as numbers of participants or number of sprints, so that the agile method can work best for me",
                        "As a team-member I want to use it to log additional scrums or events, so that I can communicate with the team.",
                        "As TM I would like to be able to access all user stories made, so that I can choose which go in what sprints",
                        "As a TM I would like to access metrics such as burn down charts, so that I can visualise progress and comprehend it more thoroughly",
                        "As an agile developer I want to use it as a reminder, so that I can make sure I don't stray away from my good habits.",
                        "As a team-member I would like to be able to verify the prioritisation of the backlog, so that we have the possibility to adapt our estimates regularly",
                        "As a team-member/moderator I would like to be able to use poker planning, so that I can work with my team to estimate task duration",
                        "As a TM I would like to get notified when I forget something such as a daily scrum, so that I don't get into the habit of missing them"]
    for uS in range(len(exampleUserStory)):
        if uS <= 3:
            task = Task(name="dummy data "+str(uS), description = exampleUserStory[uS], creation = datetime.strptime('25/03/2022', '%d/%m/%Y').date(), status = 2, pokerScore = random.choice(pokerPlanningList), sprint_id = 1, project_id  = 1)
        elif uS <= 6:
            task = Task(name="dummy data "+str(uS), description = exampleUserStory[uS], creation = datetime.strptime('25/03/2022', '%d/%m/%Y').date(), status = 2, pokerScore = random.choice(pokerPlanningList), sprint_id = 2, project_id  = 1)
        elif uS <= 9:
            task = Task(name="dummy data "+str(uS), description = exampleUserStory[uS], creation = datetime.strptime('25/03/2022', '%d/%m/%Y').date(), status = 2, pokerScore = random.choice(pokerPlanningList), sprint_id = 3, project_id  = 1)
        else:
            task = Task(name="dummy data "+str(uS), description = exampleUserStory[uS], creation = datetime.strptime('25/03/2022', '%d/%m/%Y').date(), status = 0, pokerScore = random.choice(pokerPlanningList), sprint_id = 3, project_id  = 1)
        db.session.add(task)

    
    db.session.commit()


"""
Description:
    This is a function to facilitate the creation of a new user in the rest of the code.
"""
def createUser(username, name, firstname, passwd, blocked = False, group = False):
# date pas sûre
    user1 = User(username=username, name=name, firstname=firstname,
            blocked=blocked, group=group)
    
    user1.set_password(passwd)

    return user1

def createAdmin():
    user1 = User(
                username='admin123', 
                name='Ken', 
                firstname='Thompson',
                passwd_hash=generate_password_hash('admin123##!wqeq'), 
                blocked=False, 
                group=True
            )
    
    user1.set_password("admin123##!wqeq")

    db.session.add(user1)

    db.session.commit()    
