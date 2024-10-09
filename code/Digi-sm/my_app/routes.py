from cgitb import html
from my_app import app
from .models import *
from flask import render_template, redirect, request, url_for, session, flash
from flask_login import login_user, logout_user, login_required, current_user
from .forms import RegisterForm, LoginForm, TaskForm , ProjectForm, AddUserToProject, AddFriend
from .login_manager import *
from datetime import date
import json
from .nonFlaskFunctions import updt_order, defaultOrder, userStoryGraphCalculator, nbTaskDoing, nbRemainingTask, nbTask


#-------------------- This is the home route, this is the heart of the website --------------------

"""
Description:
    This is the route for the home page of the application.
    This requires the user to be logged in.

Parameters:
    None

Returns:
    render_template: the home page of the application rendered with flask
    render_template: redirects to the help message of the home page

Specification last modified: 12-02-2023
"""
@app.route('/' , methods=['GET', 'POST'])
@login_required
def show_tasks():

    
    #this updates the order of the user stories in the database before reloading them below
    if request.method == "POST":
        #print("activated")
        
        allKeys = request.form.keys()

        assert allKeys != None, "allKeys is None. Post method is not working properly"

        if "creation" in allKeys:
            #print(request.form["creation"])
            json.loads(request.form["creation"])
           
        
        if "data" in allKeys:
            listUserStories = request.form["data"]
            
            if listUserStories != "":

                listUserStories = json.loads(listUserStories)
                updt_order(listUserStories)
        
        if "step" in allKeys:
            stepsSprint = request.form["step"]
            stepsSprint = json.loads(stepsSprint)

            #print(stepsSprint)
    
            if str(stepsSprint[1]) == "forward" and int(stepsSprint[0])%5 == 0:
                session["sprintMutliple"]+=1
            elif stepsSprint[1] == "back":
                session["sprintMutliple"]-=1
        
        
    #loads 5 sprints at a time to prevent clutter based on sprint number
    #print(session["sprintMutliple"])
    assert type(session["sprintMutliple"]) == int

    if session["sprintMutliple"] > 0:
        sprints = Sprint.query.filter_by(project_id=session["project"]).all()
        sprints = sprints[session["sprintMutliple"]*5:session["sprintMutliple"]*5+5]
    else:
        sprints = Sprint.query.filter_by(project_id=session["project"]).all()
        sprints = sprints[:5]

    if session["sprintMutliple"] == 0:
        sprintOrder = [1,2,3,4,5]
    else:
        sprintOrder = list(map((lambda x:x+5), [1,2,3,4,5]))
    

    lastSprint = True
    if len(sprints) > 0:
        if sprints[-1].id == Sprint.query.filter_by(project_id=session["project"]).all()[-1].id:
            lastSprint = False	
        
    if session["sprint"] != 0:
        tasks = Task.query.filter_by(sprint_id=session["sprint"]).all()
    else:
        tasks = []
        
    
    #re-arrange task list in the right order 
    taskOrder = TaskSprintOrder.query.filter_by(sprint_id=session["sprint"]).all()

    taskOrderTuples = []

    for i in range(len(taskOrder)):
        taskOrderTuples.append((taskOrder[i].task_id, taskOrder[i].order))
    #now we have a list of tuples with the task id and the order ex: [(1, 2), (2, 1), (3, 3)] and need to re-arrange the task list

    if taskOrderTuples == []:
        defaultOrder(tasks, session["sprint"])
    else:
        #there is only a need to sort the order of the userstories if its not a default order
        taskOrder = sorted(taskOrderTuples, key = lambda tuple: tuple[1])
        
        taskOrderIndex = []
        for i in range(len(taskOrder)):
            taskOrderIndex.append(taskOrder[i][0])

        tasksOrdered = []
        for userStoryId in taskOrderIndex:
            tasksOrdered.append(next((x for x in tasks if x.id == userStoryId), None))

        tasks = tasksOrdered
    
    nb_tot = nbTask()
    nb_toDo = nbRemainingTask()
    nb_Doing = nbTaskDoing()
    
    dataBurnDown = userStoryGraphCalculator()
    creationDates = dataBurnDown[3]
    #add project creation date to the front of the list of dates for the x axis
    creationDates.insert(0, dataBurnDown[2])

    points = [dataBurnDown[0]]
    pointDifference = dataBurnDown[0]
    for point in dataBurnDown[1]:
        pointDifference -= point
        points.append(pointDifference)


    #lists the amount of notifications a user has 
    notificationProject = ProjectRequest.query.filter_by(user_id=current_user.id).all()
    notificationFriendRequest = FriendRequest.query.filter_by(friend_id=current_user.id).all()
    notificationAmount = notificationProject + notificationFriendRequest
    notificationAmount = len(notificationAmount)

    tasksOnProject = Task.query.filter_by(project_id=session["project"]).all()
    amountOfProjects = len(db.session.query(association_user_project.c.project_id).filter(association_user_project.c.user_id == current_user.id).all())

    #this means there is nothing in the project yet and its the first project so the tutorial will be shown
    if len(sprints) == 0 and len(tasksOnProject) == 0 and amountOfProjects == 1:
        return render_template('helpMessageHome.html', messageId = 8, sprintOrder = sprintOrder, currentSprint = session["sprint"], sprints = sprints, lastSprint = lastSprint, toDo_list=tasks, nb_tot=nb_tot, nb_toDo=nb_toDo, nb_Doing=nb_Doing, admin=current_user.group, pokerPlan = pokerPlanningList, creationDate = creationDates, points = points, home = True, notificationAmount = notificationAmount)
    

    try:
        messageId = session["helpMessageId"]
        session.pop("helpMessageId")
        return render_template('helpMessageHome.html', messageId = messageId, sprintOrder = sprintOrder, currentSprint = session["sprint"], sprints = sprints, lastSprint = lastSprint, toDo_list=tasks, nb_tot=nb_tot, nb_toDo=nb_toDo, nb_Doing=nb_Doing, admin=current_user.group, pokerPlan = pokerPlanningList, creationDate = creationDates, points = points, home = True, notificationAmount = notificationAmount)
    except KeyError: 
        return render_template('timeline.html', sprintOrder = sprintOrder, currentSprint = session["sprint"], sprints = sprints, lastSprint = lastSprint, toDo_list=tasks, nb_tot=nb_tot, nb_toDo=nb_toDo, nb_Doing=nb_Doing, admin=current_user.group, pokerPlan = pokerPlanningList, creationDate = creationDates, points = points, home = True, notificationAmount = notificationAmount)


#-------------------- ROUTES THAT DEAL WITH SPRINTS --------------------

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
    This route is used to shift the timeline to the left or right depending on the user input.

Parameters:
    None

Returns:
    redirect: redirect the user to the home page
"""
@app.route("/shift_sprint/", methods = ['GET', 'POST'])
@login_required
def shift_sprint():

    if request.method == "POST":
        stepsSprint = request.form["data"]

        stepsSprint = json.loads(stepsSprint)

        #check last created sprint for project and if the view needs to change
        lastSprintId = len(Sprint.query.filter_by(project_id=session["project"]).all())
        assert lastSprintId > 0

        if (lastSprintId-1)//5 != session["sprintMutliple"]:
            session["sprintMutliple"] = (lastSprintId-1)//5

    return redirect('/', code =204)
    


"""
Description:
    Coomunites with ajax to get the list of user stories selected by the user and creates a new sprint with them.
    This function takes the list and update what user story belongs to what sprint.

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

        listUserStories = json.loads(listUserStories)

        #need to select a min of 1 user story to create a sprint
        assert len(listUserStories) > 0

        #create new sprint and add list of user stories selected to it
        today = date.today()

        newSprint = Sprint(
                        creation = today.strftime("%d/%m/%Y"),
                        status = 0,
                        project_id = session["project"]
                        )
        
        

        db.session.add(newSprint)
        db.session.commit()

        #adds userstories to the sprint and initialises their order in the table when showed im table

        defaultOrder(listUserStories, newSprint.id)
        
        

        session["sprint"] = newSprint.id
        #sprint = Sprint(name = "Sprint 1", project_id = session["project"])
        #db.session.add(sprint)
        #db.session.commit()

        db.session.commit()
        

    listUserStories = Task.query.filter_by(project_id=session["project"], sprint_id = None).all()
    lastSprint = Sprint.query.filter_by(project_id=session["project"]).all()

    if len(lastSprint) > 0:
        listLastSprintUserStories = Task.query.filter_by(project_id=session["project"], sprint_id = lastSprint[-1].id).all()

        allDone = True
        for userStories in listLastSprintUserStories:
            if userStories.status != 2:
                allDone = False
                break
    else:
        allDone = True
    
    sizeList = len(listUserStories)
    return render_template("sprintCreation.html", listUserStories = listUserStories, sizeList = sizeList, allDone = allDone)


"""
Description:
    This route is used to update the order of the user stories in the sprint.
    It does so by recovering the new order of the user stories from the front end and updating the database with the new order.

Parameters:
    None

Returns:
    redirect: returns a 204 status code to the front end to indicate that the request was successful as the frontend does the redirecting

Specification last modified: 29-03-2023
"""
@app.route("/update_order", methods = ['GET', 'POST'])
@login_required
def update_order():

    if request.method == "POST":
        listUserStories = request.form["data"]

        listUserStories = json.loads(listUserStories)

        assert len(listUserStories) > 0

        updt_order(listUserStories)

    return ('', 204)


#-------------------- ROUTES THAT DEAL WITH PROJECTS --------------------


"""
Description:
    This route is used to create a new project by adding the name and description from the frontend to the database.

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

        amountOfProjectsBef = len(db.session.query(association_user_project.c.project_id).filter(association_user_project.c.user_id == current_user.id).all())
        
        newProject = Project(name=form.name.data, description=form.description.data, creation = today.strftime("%d/%m/%Y"), status=True)
    
        db.session.add(newProject)
        newProject.user.append(current_user)
        
        db.session.commit()

        amountOfProjectsAfter = len(db.session.query(association_user_project.c.project_id).filter(association_user_project.c.user_id == current_user.id).all())

        assert amountOfProjectsAfter == amountOfProjectsBef + 1

        session["project"] = newProject.id
        session["sprint"] = 0
        
            
 
        session["sprint"] = 0
        session["sprintMutliple"] = 0 

        assert session["sprintMutliple"] >= 0
        

        return redirect('/', code=302)
    else:
        return render_template("createProjects.html")

"""
Description:
    This route is used to mark a project as finished or to resume an old project and
    have it reflect in the database.
    
Parameters:
    project_id: the id of the project to be marked as finished or resumed

Returns:
    redirect: redirects the user to the redirectProjects page

Specification last modified: 30-03-2023
"""
@app.route("/finishProject/<int:project_id>")
@login_required
def finishProject(project_id):

    project = Project.query.filter_by(id=project_id).first()

    assert project != None

    project.status = not project.status

    db.session.commit()
    
    return redirect('/redirectProjects', code=302)

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

    
    sprint1 = Sprint.query.filter_by(project_id=project_id).order_by(Sprint.id.desc()).first()


    session["project"] = project_id

    if sprint1 == None:
        session["sprint"] = 0
        session["sprintMutliple"] = 0 
    else:
        session["sprint"] = sprint1.id
        session["sprintMutliple"] = (len(Sprint.query.filter_by(project_id=session["project"]).all())-1)//5

        assert session["sprintMutliple"] >= 0

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
        #This allows the extract the prjects the user is part of through the association table
        projects = db.session.query(association_user_project.c.project_id).filter(association_user_project.c.user_id == current_user.id).all()
        projectObjectList = []
        for project in projects:
            projectObjectList.append(Project.query.filter_by(id=project[0]).first())

        #the 5 corresponds to the messageId which is used to display the correct message in the front-end (this can be seen in the projectChoice.html file which is the root
        # of the project choice page)
        #print(projectObjectList)
        if len(projectObjectList) == 0:
            session["helpMessageId"] = 5

        try:
            messageId = session["helpMessageId"]
            session.pop("helpMessageId")
            #print(messageId)
            return render_template('helpMessageProject.html', user=current_user, projects = projectObjectList, messageId = messageId, dayPassed = False)
        except KeyError: 
            
            dayPassed = False
            day = user.last_seen.day
            if int(day) != int(datetime.now().day):
                dayPassed = True    
                user.last_seen = datetime.now()
                db.session.commit()

            return render_template('scrollProjects.html', user=current_user, projects = projectObjectList, dayPassed = dayPassed)
        #print(projects)

    return render_template('error.html', status = 403, message='You have been blocked by the admin.')


#-------------------- ROUTES THAT DEAL WITH USERS --------------------
   
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

    assert user_info != None

    if request.method == "POST":
        
        user_info.name = form.name.data
        user_info.firstname = form.firstname.data
        
        #print(form.passwd.data)
        if form.passwd.data != form.passwd_confirm.data:
            #print("password changed")
            return render_template('profile.html', user_info = user_info, errorPassword="Passwords do not match.")
        else:
            if form.passwd.data != "":
                user_info.set_password(form.passwd.data)
            
            

        db.session.commit()

        #check if the user has been updated
        user_check = User.query.filter_by(username=current_user.username).first()
        assert user_check.name == form.name.data

        return redirect('/', code=302)
    else:
        return render_template('profile.html', user_info = user_info)

"""
@deprecated replaced by the team route

Description:
    This is the page to see what users are working on the project.

Parameters:
    None

Returns:
    render_template: the html page showing all the users on the project.

Specification last modified: 12-02-2023
"""
@app.route('/userOnProject', methods=['GET', 'POST'])
@login_required
def userOnProject():
    
    if current_user.group == True:
        nb_tot = nbTask()
        nb_toDo = nbRemainingTask()
        tasks = Task.query.filter_by(sprint_id=session["sprint"]).all()
        
        # FETCH ALL THE RECORDS IN THE RESPONSE
        userListOnProject = Project.query.filter_by(id = session["project"]).all()
        #print(userListOnProject)
        #print(userListOnProject[0].user)
        userListOnProject = userListOnProject[0].user
        
        return render_template('userOnProject.html', toDo_list=tasks, nb_tot=nb_tot, nb_toDo=nb_toDo, admin=current_user.group, user_list = userListOnProject )


"""
Description:
    This function is used by receiving a username from the frontend and determining if its valid, if it is its sends a project request.
    
Parameters:
    None it takes a flask form
    
Returns:
    render_template: the html page showing all the users on the project.

Specification last modified: 02-04-2023
"""
@app.route('/addUserProjectByUsername', methods=['GET', 'POST'])
@login_required
def addUserProjectByUsername():
    
    form = AddUserToProject()

    
    if request.method == 'POST':

        _usernameRequested = request.form["username hidden"]
        projectId = session["project"]
        usersIdOnProject = db.session.query(association_user_project.c.user_id).filter(association_user_project.c.project_id == projectId).all()

        userOnProject = []
        for user in usersIdOnProject:
            userOnProject.append(User.query.filter_by(id=user[0]).first())

        #this assertion can be made as at least the creator is on the project
        assert userOnProject != None
        #print(userOnProject)
        #print(userOnProject)
        userThere = False
        #checks if the user is already on the project
        for userObject in userOnProject:
            #print(userObject.username)
            #print(_usernameRequested)
            if userObject.username == _usernameRequested:
                userThere = True
        
        if userThere == True:                  
            message = "User already on the project"
        else:
            usernameToUser = User.query.filter_by(username = _usernameRequested).first()
            
            if usernameToUser == None:
                message = "User does not exist"
            else:
                projectRequest = ProjectRequest.query.filter_by(project_id = projectId, user_id = usernameToUser.id).first()
                
                if projectRequest == None:  
                    
                    newRquest = ProjectRequest(project_id = projectId, user_id = usernameToUser.id)
                    db.session.add(newRquest)
                    db.session.commit()
                    projectRequest = ProjectRequest.query.filter_by(project_id = projectId, user_id = usernameToUser.id).first()  
                    message = "Request to join the project was sent"
                    
                else:
                    message = "Request to join the project has already been sent"
        
        return render_template('team.html', admin=current_user.group, user_list = userOnProject,currentUser = current_user.id, response = message) 
    else:
        return render_template("createProjects.html")


"""
Description:
    This function is called when a button is clicked allowing to add a user to the project directly.
    
Parameters:
    None it takes a flask form
    
Returns:
    render_template: the html page showing all the users on the project.

Specification last modified: 02-04-2023
"""
@app.route('/addUserProjectButton', methods=['GET', 'POST'])
@login_required
def addUserProjectButton():  

    projectId = session["project"]

    user_id = request.form["data"]
    user_id = json.loads(user_id)
    #print(user_id)

    newProjectRequest = ProjectRequest(project_id = projectId, user_id = user_id)
    db.session.add(newProjectRequest)
    db.session.commit()

    return ('', 204)
    


"""
Description:
    This is the page to see your friends list and to add new ones.

Parameters:
    None

Returns:
    render_template: the html page showing all your friends

Specification last modified: 25-02-2023
"""
@app.route("/friends", methods = ['GET', 'POST'])
@login_required
def friends():

    form = AddFriend()

    friendsab = FriendsList.query.filter_by(user_id = current_user.id).all()
    friendsba = FriendsList.query.filter_by(friend_id = current_user.id).all()

    usersIdOnProject = db.session.query(association_user_project.c.user_id).filter(association_user_project.c.project_id == session["project"]).all()
    userOnProject = []
    for user in usersIdOnProject:
        userOnProject.append(User.query.filter_by(id=user[0]).first().id)

    #anonymous function to check if a user is on the project while loading the friends list
    isOnProject = lambda num: "0" if num in userOnProject else ("1" if ProjectRequest.query.filter_by(user_id = num, project_id = session["project"]).first() != None else "2")

    friendsA = map(lambda x: (isOnProject(x.friend_id), User.query.filter_by(id=x.friend_id).first()), friendsab)
    friendsB = map(lambda x: (isOnProject(x.user_id), User.query.filter_by(id=x.user_id).first()), friendsba)
    friends = list(friendsA) + list(friendsB)
    #print(friends)

    if len(friendsab) > 0 or len(friendsba) > 0:
        assert len(friends) > 0

    if request.method == "GET":
        request.args.get("username")


    if request.method == "POST":
        _username = request.form ["username hidden"]
        
        if _username == current_user.username:
            message = "You can't add yourself as a friend!"
            return render_template('Friends.html', user=current_user, friends=friends, response=message)


        _friend = User.query.filter_by(username=_username).first()

        isFriendab = FriendsList.query.filter_by(user_id = current_user.id, friend_id = _friend.id).first()
        isFriendba = FriendsList.query.filter_by(user_id = _friend.id, friend_id = current_user.id).first()

        if isFriendab is None:
            isFriendab = False
        else:
            isFriendab = True
        
        if isFriendba is None:
            isFriendba = False
        else:
            isFriendba = True
            
        assert not(isFriendab == True and isFriendba == True)
        #print(isFriendab)
        #print(isFriendba)

        if isFriendab != (not isFriendba):

            requestsSent = FriendRequest.query.filter_by(user_id = current_user.id, friend_id = _friend.id).first()
            requestsReceived = FriendRequest.query.filter_by(user_id = _friend.id, friend_id = current_user.id).first()

            if requestsSent is None:

                if requestsReceived is not None:
                    message = "They already sent you a friend request! Check your notifications!"
                else:
                    newRequest = FriendRequest(user_id = current_user.id, friend_id = _friend.id)
                    db.session.add(newRequest)
                    db.session.commit()
                    message = "Friend request was sent"
            else:
                message = "Friend request already sent"

            return render_template('Friends.html', user=current_user, friends=friends, response=message)
        else:
            message = "User is already your friend!"
            return render_template('Friends.html', user=current_user, friends=friends, response=message)
    else:
        return render_template('Friends.html', user=current_user, friends=friends)



"""
Description:
    This is the team page allowing to see which users are working on the project and add new users to the project.
    As well as a view of their friendlist in order to quickly add people in their friendlist to the project.

Parameters:
    None

Returns:
    render_template: the admin page of the application rendered with flask

Specification last modified: 12-02-2023
"""
@app.route('/team', methods=['GET', 'POST'])
@login_required
def team():
        
    # FETCH ALL THE RECORDS IN THE RESPONSE

    usersIdOnProject = db.session.query(association_user_project.c.user_id).filter(association_user_project.c.project_id == session["project"]).all()
    userOnProject = []
    for user in usersIdOnProject:
        userOnProject.append(User.query.filter_by(id=user[0]).first().id)

    isOnProject = lambda num: "0" if num in userOnProject else ("1" if ProjectRequest.query.filter_by(user_id = num, project_id = session["project"]).first() != None else "2")

    friendsab = FriendsList.query.filter_by(user_id = current_user.id).all()
    friendsba = FriendsList.query.filter_by(friend_id = current_user.id).all()
    friendsA = map(lambda x: (isOnProject(x.friend_id), User.query.filter_by(id=x.friend_id).first()), friendsab)
    friendsB = map(lambda x: (isOnProject(x.user_id), User.query.filter_by(id=x.user_id).first()), friendsba)
    friends = list(friendsA) + list(friendsB)

    if len(friendsab) > 0 or len(friendsba) > 0:
        assert len(friends) > 0

    projectId = session["project"]

    usersIdOnProject = db.session.query(association_user_project.c.user_id).filter(association_user_project.c.project_id == projectId).all()

    userOnProject = []
    for user in usersIdOnProject:

        userOnProject.append(User.query.filter_by(id=user[0]).first())

    #this assertion can be made as at least the creator is on the project
    assert userOnProject != None
    #print(userOnProject)

    try:
        messageId = session["helpMessageId"]
        session.pop("helpMessageId")
        return render_template('helpMessageTeam.html', admin=current_user.group, user_list = userOnProject,currentUser = current_user.id, friends = friends, messageId=messageId)
    except KeyError: 
        return render_template('team.html', admin=current_user.group, user_list = userOnProject,currentUser = current_user.id, friends = friends)
     



#-------------------- ROUTES THAT DEAL WITH SPECIAL USER ACTIONS --------------------


"""
Description:
    This route is an admin feature allowing to block users from the application.

Parameters:
    user_id1: the id of the user to be blocked

Returns:
    render_template error: the error page in case of an issue whilst blocking the user
    render_template team: refreshes the page and shows the user as blocked
    
Specification last modified: 12-02-2023
"""
@app.route("/bloc_user/<int:user_id1>")
@login_required
def bloc_user(user_id1):


    _user = User.query.filter_by(id=user_id1).first()
    
    if _user != None:

        _user.blocked = not _user.blocked
        db.session.commit()

        projectId = session["project"]
        assert type(projectId) == int

        usersIdOnProject = db.session.query(association_user_project.c.user_id).filter(association_user_project.c.project_id == projectId).all()

        userOnProject = []
        for user in usersIdOnProject:

            userOnProject.append(User.query.filter_by(id=user[0]).first())

        #this assertion can be made as at least the creator is on the project
        assert userOnProject != None

        return redirect(url_for('team')) 
    else:
        return render_template('error.html', status=404, message="Cannot block this user (user not found).")

"""
Description:
    This route is an admin feature allowing to make other users admins.

Parameters:
    user_id1: the id of the user to be made admin

Returns:
    render_template error: the error page in case of an issue whilst making the user admin
    render_template team: refreshes the page and shows the user as admin

Specification last modified: 12-02-2023
"""
@app.route("/change_group/<int:user_id1>")
@login_required
def change_group(user_id1):

    _user = User.query.filter_by(id=user_id1).first()

    if _user != None:

        _user.group = not _user.group
        db.session.commit()

        return redirect(url_for('team'))
    else:
        return render_template('error.html', status=404, message="Cannot change group of user (user not found).")
    
"""
Description:
    This is the admin page allowing access to the admin features such as seeing all users of the website.

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
        
        # FETCH ALL THE RECORDS IN THE RESPONSE
        userList = User.query.all()
        #print(userList)
        
        return render_template('team.html', admin=current_user.group, user_list = userList)
    



#-------------------- ROUTES THAT DEAL WITH NOTIFICATIONS --------------------


"""
Description:
    This page is used to see the notifications that the user received.
    Wether its a friend request or a request to join a project.

Parameters:
    None

Returns:
    render_template: the notification page of the application rendered with flask
"""
@app.route('/notification', methods=['GET', 'POST'])
@login_required
def notification():
    

    current_user_id = current_user.id
    
    projectRequests = ProjectRequest.query.filter_by(user_id = current_user_id).all()

    friendRequests = FriendRequest.query.filter_by(friend_id = current_user_id).all()

    projectNames = []
    friendNames = []

    for project in projectRequests:
        projectNames.append([0, Project.query.filter_by(id = project.project_id).first().name])

    for friend in friendRequests:
        friendNames.append([1, User.query.filter_by(id = friend.user_id).first().username])

    notifications = projectNames + friendNames


    if request.method == "GET":
        name = request.args.get("notif_id")
        value = request.args.get("response")
        type = request.args.get("type")

        #this means its a project request and not a friend request
        if type == '0':
            project = Project.query.filter_by(name = name).first()
            user = User.query.filter_by(id = current_user_id).first()

            if name != None and len(projectRequests) > 0:

                #delete the request from the table
                projectRequest = ProjectRequest.query.filter_by(project_id = project.id, user_id = current_user_id).first()

                #this just prevents the user to return and reload the same page with the same arguments thus deleting a none type
        
                if projectRequest != None:
                    db.session.delete(projectRequest)
                    
                    if value == 'true':
                        
                        #add the user to the project
                        project.user.append(user)
                db.session.commit()
        
        else:
            
            friend = User.query.filter_by(username = name).first()
            user = User.query.filter_by(id = current_user_id).first()
            
            #there is no way to delete users for now so they should both exist
            assert user != None

            if name != None and len(friendRequests) > 0:
                
                #delete the request from the table
                friendRequest = FriendRequest.query.filter_by(user_id = friend.id, friend_id = current_user_id).first()

                #this just prevents the user to return and reload the same page with the same arguments thus deleting a none type
                if friendRequest != None:
                    db.session.delete(friendRequest)
              
                    if value == 'true':
                      
                        friendListEntry = FriendsList(user_id = current_user_id, friend_id = friend.id)
                        db.session.add(friendListEntry)
                    
                db.session.commit()

    #need to refresh the project requests to be shown on the page
    projectRequests = ProjectRequest.query.filter_by(user_id = current_user_id).all()

    friendRequests = FriendRequest.query.filter_by(friend_id = current_user_id).all()

    projectNames = []
    friendNames = []

    for project in projectRequests:
        projectNames.append([0, Project.query.filter_by(id = project.project_id).first().name])

    for friend in friendRequests:
        friendNames.append([1, User.query.filter_by(id = friend.user_id).first().username])

    notifications = projectNames + friendNames


    return render_template('notifications.html', notifications = notifications)



#-------------------- ROUTES THAT DEAL WITH USER STORIES --------------------


"""
Description:
    This route is used to create a new task meaning a new user story by receiving information from the form.
    
Parameters:
    None
    
Returns:
    render_template: the new task page of the application rendered with flask
    render_template: renders the help messages of the user story

Specification last modified: 12-02-2023
"""
@app.route("/newTask", methods=['GET', 'POST']) 
@login_required 
def newTask():
    form = TaskForm()

    toDo_List = Task.query.filter_by(project_id = session["project"]).all()

    #rearrange user stories to be shown by the sprint they belong to 

    toDo_List = sorted(toDo_List, key=lambda x: x.sprint_id or 0, reverse=False)

    sprintsInt = []
    sprintId = 0
    for taskId in range(len(toDo_List)):
        if toDo_List[taskId].sprint_id == None:
            sprintsInt.append("Not in a sprint")
        elif toDo_List[taskId].sprint_id != toDo_List[taskId-1].sprint_id:
            sprintId+=1
            sprintsInt.append(sprintId)
        else:
            sprintsInt.append(sprintId)

    if request.method == 'POST':

        creation = date.today().strftime("%d/%m/%Y")
        
        new_task = Task(name=form.name.data, description=form.description.data, creation=creation,
                        status=0, pokerScore=form.pokerScore.data, project_id = session["project"])
    
        db.session.add(new_task)
        db.session.commit()

        #reload the page to show the new task
        toDo_List = Task.query.filter_by(project_id = session["project"]).all()
        toDo_List = sorted(toDo_List, key=lambda x: x.sprint_id or 0, reverse=False)
        
        sprintsInt = []
        sprintId = 0
        for taskId in range(len(toDo_List)):
            if toDo_List[taskId].sprint_id == None:
                sprintsInt.append("Not in a sprint")
            elif toDo_List[taskId].sprint_id != toDo_List[taskId-1].sprint_id:
                sprintId+=1
                sprintsInt.append(sprintId)
            else:
                sprintsInt.append(sprintId)
        
            
        return render_template('newTask.html', admin=current_user.group, pokerPlan = pokerPlanningList, toDo_list = toDo_List, sprintsInt = sprintsInt)
    else:
        try:
            messageId = session["helpMessageId"]
            session.pop("helpMessageId")
            return render_template('helpMessageUserStory.html', admin=current_user.group, pokerPlan = pokerPlanningList, toDo_list = toDo_List, messageId = messageId,sprintsInt = sprintsInt)
        except KeyError: 
            return render_template('newTask.html', admin=current_user.group, pokerPlan = pokerPlanningList, toDo_list = toDo_List, sprintsInt = sprintsInt)
        

# -----------
"""
@deprecated user stories are not meant to be deleted, so you can 
modify its status to done or set the poker score to 0
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

    #print(task.sprint.id)
    #print(session["sprint"])
    #print(task)
    
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
def modify(task_id):
    #print(task_id)
    task = Task.query.filter_by(id=task_id).first()
    #print(task)
    assert task != None
    
    if task == None:
        return render_template('error.html', status=404, message="Cannot modify this task (task not found).")
    else:
        form = TaskForm()
        if request.method == 'POST':
            
            creation = date.today().strftime("%d/%m/%Y")
            
            task.name = form.name.data
            task.description = form.description.data
            task.creation = creation
            task.pokerScore = form.pokerScore.data
            db.session.commit()
            
            return redirect('/', code=302)
        else:

            tasks = Task.query.filter_by(sprint_id=session["sprint"]).all()
            taskNb = len(tasks)
            #print(taskNb)
            nb_toDo = nbRemainingTask()
            return render_template('modify.html', pokerPlan = pokerPlanningList, nameTask=task.name, nameDescr=task.description, pokerScore = task.pokerScore, toDo_list=tasks, nb_tot=taskNb, nb_toDo=nb_toDo, admin=current_user.group, task_id=task_id)
    

#-------------------- ROUTES THAT DEAL WITH REGISTRATION & LOGIN --------------------

"""
Description:
    This route is used to register a new user to the application.

Parameters:
    None because all information is collected through the flask form

Returns:
    redirect: redirect to the choice of project page

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

    assert current_user.is_authenticated

    return redirect(url_for('redirectProjects'))



"""
Description:
    This route is used to log a user in to the application.

Parameters:
    None because all information is collected through the flask login form

Returns:
    render_template error: the error page in case of an issue whilst logging the user in
    render_template login: the login page is loaded.
    redirect url_for: redirect to the choice of project page

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
        assert current_user.is_authenticated
        if check_password_hash(user.passwd_hash, form.passwd.data ):
            
            #This allows the extract the prjects the user is part of through the association table
            projects = db.session.query(association_user_project.c.project_id).filter(association_user_project.c.user_id == current_user.id).all()
            projectObjectList = []
            for project in projects:
                projectObjectList.append(Project.query.filter_by(id=project[0]).first())
            
            return redirect(url_for("redirectProjects"))
    
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
    assert not current_user.is_authenticated
    return redirect(url_for('show_tasks'))



#-------------------- ROUTES THAT DEAL WITH TUTORIAL/HELP WINDOWS --------------------

"""
Description:
    This route is used for the educational popup messages containing
    information about the application and the agile development process.
    
Parameters:
    helpMessageId: the id of the message to be displayed

Returns:
    redurect url_for: the user is redirected to the route that was called before the help message was called.

Specification last modified: 12-02-2023    
"""
@app.route('/helperMessage/<int:helpMessageId>')
@login_required
def helperMessage(helpMessageId):

    #helpMessageId will determin which block will be loaded from helpMessage.html so which help message will be shown

    session["helpMessageId"] = helpMessageId


    if helpMessageId <= 3:
        return redirect(url_for('show_tasks'))
    elif helpMessageId == 4:
        return redirect(url_for('redirectProjects'))
    elif helpMessageId == 6:
        return redirect(url_for('team'))
    elif helpMessageId == 7:
        return redirect(url_for('newTask'))
    #return render_template('helpMessage.html',sprintOrder = sprintOrder, messageId=helpMessageId, sprints = sprints, toDo_list=tasks, nb_tot=nb_tot, nb_toDo=nb_toDo, nb_Doing=nb_Doing, admin=current_user.group, pokerPlan = pokerPlanningList, creationDate = creationDates, points = points)

   


