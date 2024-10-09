from cgitb import html
from my_app import app
from .models import *
from flask import render_template, redirect, request, url_for, session
from flask_login import login_user, logout_user, login_required, current_user
from .forms import RegisterForm, LoginForm, TaskForm , ProjectForm
from .login_manager import *
from datetime import date
import json

# ---------------------


"""
Description:
    This function is used to get the number of tasks in the current sprint.

Parameters:
    None

Returns:
    nb_toDo: number of tasks in the current sprint

Specification last modified: 12-02-2023
"""
def nbTask():
    nb_toDo = Task.query.filter_by(sprint_id=session["sprint"]).count()

    return nb_toDo

"""
Description:
    This function is used to get the number of tasks being done.

Parameters:
    None

Returns:
    nb_Doing: number of tasks being worked on currently

Specification last modified: 12-02-2023
"""
def nbRemainingTask():

    nb_Doing = Task.query.filter_by(sprint_id=session["sprint"], status=0).count()

    return nb_Doing

"""
Description:
    This function is used to get the number of remaining tasks in the current sprint.

Parameters:
    None

Returns:
    nb_toDo: number of remaining tasks in the current sprint

Specification last modified: 12-02-2023
"""
def nbTaskDoing():

    nb_toDo = Task.query.filter_by(sprint_id=session["sprint"], status=1).count()

    return nb_toDo

# -------------
"""
Description:
    This is the route for the home page of the application.
    This requires the user to be logged in.

Parameters:
    None

Returns:
    render_template: the home page of the application rendered with flask

Specification last modified: 12-02-2023
"""
@app.route('/', methods=['GET', 'POST'])
@login_required
def show_tasks():

    sprints = Sprint.query.filter_by(project_id=session["project"]).all()
    print(sprints)
    if session["sprint"] != 0:
        tasks = Task.query.filter_by(sprint_id=session["sprint"]).all()
    else:
        tasks = []

    
    nb_tot = nbTask()
    nb_toDo = nbRemainingTask()
    nb_Doing = nbTaskDoing()
    

    
    return render_template('charts.html', sprints = sprints, toDo_list=tasks, nb_tot=nb_tot, nb_toDo=nb_toDo, nb_Doing=nb_Doing, admin=current_user.group, pokerPlan = pokerPlanningList)


"""
Description:
    This route is used to make the sprint icons on the timeline clickable and to load the tasks of the selected sprint.

Parameters:
    sprint_id: the id of the sprint to load

Returns:
    redirect: redirect the user to the home page

Specification last modified: 22-02-2023
"""
@app.route("/load_sprint/<int:sprint_id>", methods = ['GET', 'POST'])
@login_required
def load_sprint(sprint_id):

    sprint = Sprint.query.filter_by(id=sprint_id).first()

    assert sprint != None

    session["sprint"] = sprint_id
    
    return redirect('/', code=302)
    


"""
Description:

    Coomunication with through ajax to get the list of user stories selected by the user and create a new sprint with them.
    This function takes the list and update what user list belongs to what  sprint.

Parameters:
    None

Returns:
    redirect: redirect the user to the home page

Specification last modified: 25-02-2023

"""
@app.route("/create_sprint/", methods = ['GET', 'POST'])
@login_required
def create_sprint():

    if request.method == "POST":
        listUserStories = request.form["data"]

        print("this is the list")
        print(listUserStories)

        listUserStories = json.loads(listUserStories)

        print(listUserStories)

        #create new sprint and add list of user stories selected to it
        today = date.today()

        newSprint = Sprint(
                        creation = today.strftime("%d/%m/%Y"),
                        status = 0,
                        project_id = session["project"]
                        )
        db.session.add(newSprint)

        for userStory in listUserStories:
            taskUpd = Task.query.filter_by(id = int(userStory)).first()
            taskUpd.sprint_id = newSprint.id

        #sprint = Sprint(name = "Sprint 1", project_id = session["project"])
        #db.session.add(sprint)
        #db.session.commit()

        db.session.commit()

    listUserStories = Task.query.filter_by(project_id=session["project"], sprint_id = None).all()

    return render_template("sprintCreation.html", listUserStories = listUserStories)


"""
Description:
    This route is used to create a new project.

Parameters:
    None

Returns:    
    render_template: the create project page of the application rendered with flask

Specification last modified: 26-02-2023

"""
@app.route("/createProject", methods = ['GET', 'POST'])
@login_required
def createProject():

    form = ProjectForm()

    if request.method == 'POST':

        #make  current date
        today = date.today()
        
        newProject = Project(name=form.name.data, description=form.description.data, creation = today.strftime("%d/%m/%Y"), status=False)
    
        db.session.add(newProject)


        newProject.user.append(current_user)
        db.session.commit()

        session["project"] = newProject.id
        session["sprint"] = 0

        return redirect('/', code=302)
    else:
        return render_template("createProjects.html")
    
   


"""
Description:
    This route give the user access to their profile page allowing them to change their information
    including their passwords.
    
parameters:
    None

returns:   
    render_template: the profile page of the application rendered with flask
    redirect: redirect the user to the home page

Specification last modified: 12-02-2023
"""
@app.route("/profile", methods = ['GET', 'POST'])
@login_required
def show_profile():

    form = RegisterForm()
    user_info = User.query.filter_by(username=current_user.username).first()


    if request.method == "POST":

        _date = request.form ["time-date"]

        birthdate = _date[8:10] +"/" + _date[5:7] +"/" + _date[0:4]
        
        user_info.name = form.name.data
        user_info.firstname = form.firstname.data
        user_info.birthday = birthdate
        
        if form.passwd == form.passwd_confirm and form.passwd != None:
            new_password = generate_password_hash(form.passwd)
            user_info.passwd_hash = new_password
            

        db.session.commit()

        return redirect('/', code=302)
    else:
        return render_template('profile.html', user_info = user_info)

"""
Description:
    This is the admin page allowing access to the admin features.

Parameters:
    None

Returns:
    render_template: the admin page of the application rendered with flask

Specification last modified: 12-02-2023
"""
@app.route('/admin', methods=['GET', 'POST'])
@login_required
def show_users():
    if current_user.group == True:
        nb_tot = nbTask()
        nb_toDo = nbRemainingTask()
        tasks = Task.query.filter_by(sprint_id=session["sprint"]).all()
        
        # FETCH ALL THE RECORDS IN THE RESPONSE
        userListOnProject = Project.query.filter_by(id = session["project"]).all()
        print(userListOnProject)
        print(userListOnProject[0].user)
        userListOnProject = userListOnProject[0].user
        
        return render_template('admin.html', toDo_list=tasks, nb_tot=nb_tot, nb_toDo=nb_toDo, admin=current_user.group, user_list = userListOnProject )

# -------------------

"""
Description:
    This route is used to create a new task.
    
Parameters:
    None
    
Returns:
    render_template: the new task page of the application rendered with flask
    redirect: redirect the user to the home page
    
Specification last modified: 12-02-2023
"""
@app.route("/newTask", methods=['GET', 'POST']) 
@login_required 
def newTask():
    form = TaskForm()
    if request.method == 'POST':


        _date = request.form ["time-date"]
        creation = _date[8:10] +"/" +  _date[5:7] +"/" +  _date[0:4]
        
        new_task = Task(name=form.name.data, description=form.description.data, creation=creation,
                        status=0, pokerScore=form.pokerScore.data, sprint_id=session["sprint"], project_id = session["project"])
    
        db.session.add(new_task)
        db.session.commit()
            
        return redirect('/', code=302)
    else:
        return render_template('newTask.html', admin=current_user.group, pokerPlan = pokerPlanningList)

# -----------
"""
Description:
    This route is used to delete a task from the database.

Parameters:
    task_id: the id of the task to be deleted from the database

Returns:
    render_template: the error page in case of an issue whilst deleting the task
    redirect: redirect the user to the home page thus reloading the page after the task has been deleted
"""
@app.route("/delete/<int:task_id>")
@login_required
def delete(task_id):

    task = Task.query.filter_by(id=task_id).first()
    
    if task != None or task.user != current_user:
    
        Task.query.filter_by(id=task_id).delete()
        db.session.commit()

        return redirect('/', code=302)
    else:
        return render_template('error.html', status=404, message="Cannot delete this task (task not found).")

# -------------
"""
Description:
    This route is used to modify the status of a task.

Parameters:
    task_id: the id of the task to be modified

Returns:
    render_template: the error page in case of an issue whilst modifying the task
    redirect: redirect the user to the home page thus reloading the page after the task has been modified

Specification last modified: 12-02-2023
"""
@app.route("/check_uncheck/<int:task_id>")
@login_required
def check_uncheck(task_id):
    task = Task.query.filter_by(id=task_id).first()

    print(task.sprint.id)
    print(session["sprint"])
    print(task)
    
    if task is None or str(task.sprint.id) != str(session["sprint"]):
        return render_template('error.html', status=404, message="Cannot check/uncheck this task (task not found).")
    else:  
        task.status = (task.status + 1)%3
        db.session.commit()
        return redirect('/', code=302)
    
# -------------
"""
Description:
    This route is used to modify a task and its attributes.

Parameters:
    task_id: the id of the task to be modified

Returns:
    render_template error: the error page in case of an issue whilst modifying the task
    render_template modify: the modified task page of the application rendered with flask
    redirect: redirect the user to the home page thus reloading the page after the task has been modified

Specification last modified: 12-02-2023
"""
@app.route("/modify/<int:task_id>", methods=['GET', 'POST'])
@login_required
def modal(task_id):
    task = Task.query.filter_by(id=task_id).first()
    
    if task is None or str(task.sprint.id) != str(session["sprint"]):
        return render_template('error.html', status=404, message="Cannot modify this task (task not found).")
    else:
        form = TaskForm()
        if request.method == 'POST':
            
            _date = request.form ["time-date"]
            creation = _date[8:10] +"/" +  _date[5:7] +"/" +  _date[0:4]
            
            task.name = form.name.data
            task.description = form.description.data
            task.creation = creation
            db.session.commit()
            
            return redirect('/', code=302)
        else:
            tasks = Task.query.filter_by(sprint_id=session["sprint"]).all()
            taskNb = len(tasks)
            print(taskNb)
            nb_toDo = nbRemainingTask()
            return render_template('modify.html', nameTask=task.name, nameDescr=task.description, toDo_list=tasks, nb_tot=taskNb, nb_toDo=nb_toDo, admin=current_user.group, task_id=task_id)
    


# -------------
"""
Description:
    This route is an admin feature allowing to block users from the application.

Parameters:
    user_id1: the id of the user to be blocked

Returns:
    render_template error: the error page in case of an issue whilst blocking the user
    render_template admin: refreshes the page and shows the user as blocked
    
Specification last modified: 12-02-2023
"""
@app.route("/bloc_user/<int:user_id1>")
@login_required
def bloc_user(user_id1):

    _user = User.query.filter_by(id=user_id1).first()
    
    if _user != None:

        _user.blocked = not _user.blocked
        db.session.commit()

        
        nb_tot = nbTask()
        nb_toDo = nbRemainingTask()
        userList = User.query.all()
        return render_template('admin.html', toDo_list=current_user.tasks, nb_tot=nb_tot, nb_toDo=nb_toDo, admin=current_user.group, user_list = userList )
    else:
        return render_template('error.html', status=404, message="Cannot block this user (user not found).")

"""
Description:
    This route is an admin feature allowing to make other users admins.

Parameters:
    user_id1: the id of the user to be made admin

Returns:
    render_template error: the error page in case of an issue whilst making the user admin
    render_template admin: refreshes the page and shows the user as admin

Specification last modified: 12-02-2023
"""
@app.route("/change_group/<int:user_id1>")
@login_required
def change_group(user_id1):

    _user = User.query.filter_by(id=user_id1, group=False).first()

    if _user != None:

        _user.group = not _user.group
        db.session.commit()
        userList = User.query.all()
        
        nb_tot = nbTask()
        nb_toDo = nbRemainingTask()
        return render_template('admin.html', toDo_list=current_user.tasks, nb_tot=nb_tot, nb_toDo=nb_toDo, admin=current_user.group, user_list = userList )
    else:
        return render_template('error.html', status=404, message="Cannot change group of user (user not found).")

"""
Description:
    This route is a user feature allowing them to choose the project they want to work on.
    Aka a project management window.

Parameters:
    project_id: the id of the project chosen and to be displayed

Returns:
    render_template error: the error page in case of an issue whilst choosing the project
    render_template timeline: the timeline of the project and the html interface is loaded.

Specification last modified: 12-02-2023
"""
@app.route("/choose_project/<int:project_id>")
@login_required
def choose_project(project_id):

    
    sprint1 = Sprint.query.filter_by(project_id=project_id).first()

    """New projects have no sprints yet, this prevents a none error,
    changed render_template to redirect so no more need to load tasks here"""
    #if sprint1 != None:
    #    tasks = Task.query.filter_by(sprint_id=sprint1.id).all()
    #else:
    #    tasks = []

    

    #if tasks is None:
    #    return render_template('error.html', status=404, message="Error loading tasks.")
    #else: 
    session["project"] = project_id

    if sprint1 == None:
        session["sprint"] = 0
    else:
        session["sprint"] = sprint1.id

    return redirect(url_for('show_tasks'))


"""
Description:
    This route is made so that if a user is already logged in and working on a project,
    if they wish to see the other projects they're part of they can go back to the project
    choice page. The function simply makes sure the user hasnt been banned by an admin
    whilst his session was running.

Parameters:
    None

Returns:
    render_template error: the error page in case the user was blocked by an admin
    render_template projectChoice: the project choice page is loaded.

Specification last modified: 12-02-2023
"""
@app.route("/redirectProjects")
@login_required
def redirectProjects():


    user = User.query.filter_by(username=current_user.username).first()
    
    assert user != None
    
    if bool(user.blocked) == False:  
        projects = Project.query.join(User, Project.user).all()
        #print(projects)
        return render_template('scrollProjects.html', user=current_user, projects = projects)

    return render_template('error.html', status = 403, message='You have been blocked by the admin.')

# -------------- Registration & Log --------------

"""
Description:
    This route is used to register a new user to the application.

Parameters:
    None because all information is collected through the flask form

Returns:
    render_template error: the error page in case of an issue whilst registering the user
    render_template login: the login page is loaded.

Specification last modified: 12-02-2023
"""
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    
    if request.method == 'GET':
        return render_template('register.html', form=form, user=current_user)
    if not form.validate_on_submit():
        return render_template('register.html', form=form, user=current_user)
    
    new_user = createUser(form.username.data, form.name.data, form.firstname.data, form.passwd.data)

    #new_user.set_password(form.passwd.data)
    db.session.add(new_user)
    db.session.commit()


    login_user(new_user, remember=True, force=True)

    #This allows the extraction of the projects the user is a part of through the association table.
    #This is used by the front end but in the case of the new user returns an empty list anyways.
    projects = db.session.query(association_user_project.c.project_id).filter(association_user_project.c.user_id == current_user.id).all()

    assert projects == []

    return render_template('projectChoice.html', user=current_user, projects = projects)


"""
Description:
    This route is used to log a user in to the application.

Parameters:
    None because all information is collected through the flask login form

Returns:
    render_template error: the error page in case of an issue whilst logging the user in
    render_template login: the login page is loaded.
    render_template projectChoice: the project choice page is loaded allowing the user to choose his project.

Specification last modified: 12-02-2023
"""
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'GET':
        return render_template('login.html', form=form, user=current_user, error=None)
    if not form.validate_on_submit():
        return render_template('login.html', form=form, user=current_user, error=None)
    
    user = User.query.filter_by(username=form.username.data).first()
    
    if user is None:
        return render_template('login.html', form=form, user=current_user, error='This user does not exist.')
    
    if bool(user.blocked) == False:  
        login_user(user, remember=True, force=True)
        if check_password_hash(user.passwd_hash, form.passwd.data ):
            
            #This allows the extract the prjects the user is part of through the association table
            projects = db.session.query(association_user_project.c.project_id).filter(association_user_project.c.user_id == current_user.id).all()
            projectObjectList = []
            for project in projects:
                projectObjectList.append(Project.query.filter_by(id=project[0]).first())
            
            return render_template('scrollProjects.html', user=current_user, projects = projectObjectList)
    
    return render_template('error.html', status = 403, message='You have been blocked by the admin.')

# OK
"""
Description:
    This route is used to log a user out of the application.
    
Parameters:
    None
    
Returns:
    redirect url_for show_tasks: the user is redirected to the show_tasks route which reloads
    the login page with all the right information.

Specification last modified: 12-02-2023
"""
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('show_tasks'))

"""
Description:
    THis route is used for the educational popup messages containing
    information about the application and the agile development process.
    
Parameters:
    helpMessageId: the id of the message to be displayed

Returns:
    render_template helpMessage: the help message page is loaded with the right message.

Specification last modified: 12-02-2023    
"""
@app.route('/helperMessage/<int:helpMessageId>')
@login_required
def helperMessage(helpMessageId):

    #helpMessageId will determin which block will be loaded from helpMessage.html so which help message will be shown

    nb_tot = nbTask()
    nb_toDo = nbRemainingTask()
    return render_template('helpMessage.html', toDo_list=current_user.tasks, nb_tot=nb_tot, nb_toDo=nb_toDo, admin=current_user.group, pokerPlan = pokerPlanningList, messageId=helpMessageId)
   


