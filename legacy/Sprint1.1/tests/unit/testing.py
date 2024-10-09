from my_app.models import *

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
    assert project_id == 1
    
    
def test_new_task():
    
    task = Task(name = "testTask", 
                description = "testDescription",
                due = datetime.strptime('06/06/2023', '%d/%m/%Y').date(),
                status = 0,
                pokerScore = 1,
                sprint_id = 1
                sprint = 1)
    
    assert task.name == "testTask"
    assert task.description == "testDescription"
    assert task.due == datetime.strptime('06/06/2023', '%d/%m/%Y').date()
    assert task.status == 0
    assert task.pokerScore == 1
    assert task.sprint_id == 1
    assert task.sprint == 1
    

    
    
    
