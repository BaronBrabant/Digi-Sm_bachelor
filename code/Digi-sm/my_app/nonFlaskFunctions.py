from .models import *
from flask import session
from sqlalchemy import func


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

"""
Description:
    Collects all the data required to build the line chart for the burn down chart.
    This function was made to lighten the amount of code in the default home route.

Parameters:
    None
    
Returns:
    allData: a list containing all the data required to build the line chart
    
Specification last modified: 02-03-2023
"""
def userStoryGraphCalculator():
    
    allData = []
    
    totalUserStoryPoints = 0
    pointsPerSprint = []

    allUserStories = Task.query.filter_by(project_id=session["project"]).all()
    for allUserStory in allUserStories:
        totalUserStoryPoints += allUserStory.pokerScore

    projectCreationDate = Project.query.filter_by(id=session["project"]).first().creation
    
    sprints = Sprint.query.filter_by(project_id=session["project"]).all()
    creationDateSprint = []
    for sprint in sprints:
        taskPoints = db.session.query(func.sum(Task.pokerScore)).filter_by(sprint_id=sprint.id, status = 2).all()
        if taskPoints[0][0] == None:
            pointsPerSprint.append(0)
        else:
            pointsPerSprint.append(taskPoints[0][0])
        creationDateSprint.append(sprint.creation)

    allData.append(totalUserStoryPoints)
    allData.append(pointsPerSprint)
    allData.append(projectCreationDate)
    allData.append(creationDateSprint)

    return allData

"""
Description:
    This function is used to set the default order of the tasks in a sprint to be shown in the home page.

Parameters:
    listUserStories: a list of the user stories whose id need to be added to the table in order to track their order
    sprintId: the id of the sprint the user stories are in

Returns:
    None : as it just commits the change straight to the database

Specification last modified: 22-03-2023
"""
def defaultOrder(listUserStories, sprintId):

    order = 0
    #print(listUserStories)
    for userStory in listUserStories:
            
            if type(userStory) == str:
                taskUpd = Task.query.filter_by(id = int(userStory)).first()
            else:
                taskUpd = Task.query.filter_by(id = int(userStory.id)).first()
            taskUpd.sprint_id = sprintId

            newTaskSprintOrder = TaskSprintOrder(
                                                task_id = taskUpd.id,
                                                sprint_id = sprintId,
                                                order = order
                                                )
            
            order +=1
            db.session.add(newTaskSprintOrder)
    
    db.session.commit()


def updt_order(listUserStories):

    listUserStories = listUserStories[1:]
    listUserStoriesInt = [int(x) for x in listUserStories]

    taskOrder = TaskSprintOrder.query.filter_by(sprint_id=session["sprint"]).all()

    oldTaskOrder = [int(x.task_id) for x in taskOrder]

    #print("this is the order loaded from the frontend")
    #print(listUserStoriesInt)
    #print("this is the order loaded from the database")
    #print(oldTaskOrder)

    if oldTaskOrder != listUserStoriesInt:
        #the order has changed and needs to be updates in the database
        taskToDelete = TaskSprintOrder.query.filter_by(sprint_id=session["sprint"]).all()

        for task in taskToDelete:
            db.session.delete(task)

        db.session.commit()

        order = 0
        sprintId = session["sprint"]
        for userStoryId in listUserStoriesInt:

            newTaskSprintOrder = TaskSprintOrder(
                                                task_id = userStoryId,
                                                sprint_id = sprintId,
                                                order = order
                                                )
            
            order +=1
            db.session.add(newTaskSprintOrder)
        
        db.session.commit()
