from models import *


def test_new_user():
    
    user = User(
                 username='tester', 
                 name='testi', 
                 firstname='testo',
                 passwd_hash=generate_password_hash('admin123##!wqeq'), 
                 blocked=False, 
                 group=True
                )
    
    assert user.username == 'tester'
    assert user.name == 'testi'
    assert user.firstname == 'testo'
    assert user.blocked == False
    assert user.group == True
    
    
def test_new_project():
    
    project = Project( 
                        name = "test project",
                        description = "test text",
                        due = datetime.strptime('06/06/1999', '%d/%m/%Y').date(),
                        status = True
                      )
    
    assert project.name == "test project"
    assert project.description == "test text"
    assert project.due == datetime.strptime('06/06/1999', '%d/%m/%Y').date()
    assert project.status == True
    
    
def test_sprint():
    
    sprint = Sprint(
                    due = datetime.strptime('06/06/1999', '%d/%m/%Y').date(),
                    status = 0,
                    project_id = 1
                    )
    
    
    assert sprint.due == datetime.strptime('06/06/1999', '%d/%m/%Y').date()
    assert sprint.status == 0 
    assert sprint.project_id == 1

    
    
def test_new_task():
    
    task = Task(name = "testTask", 
                description = "testDescription",
                due = datetime.strptime('06/06/2023', '%d/%m/%Y').date(),
                status = 0,
                pokerScore = 1,
                sprint_id = 1)
    
    assert task.name == "testTask"
    assert task.description == "testDescription"
    assert task.due == datetime.strptime('06/06/2023', '%d/%m/%Y').date()
    assert task.status == 0
    assert task.pokerScore == 1
    assert task.sprint_id == 1
    

"""
!!!!!!!!!!!!!!!!!!!!!!!!!! Need to for code on desktop you havent pushed to test the association!!!!!!!!!!!!!
"""
def test_many_to_many():
    """
    This tests the many to many relationship between users and projects.
    """  
    
    project1 = Project( 
                        name = "test project",
                        description = "This is the p",
                        due = datetime.strptime('06/06/1999', '%d/%m/%Y').date(),
                        status = True
                      )

    project2 = Project( 
                        name = "test project 2",
                        description = "This doesnt work yet as there are no sprints or tasks implemented by default to prevent noneType error yet",
                        due = datetime.strptime('06/06/1999', '%d/%m/%Y').date(),
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

    #user1 has 2 projects and user2 has 1 project

    project1.user.append(user1)
    project2.user.append(user1)
    
    project1.user.append(user2)
    
    
    
    
    
