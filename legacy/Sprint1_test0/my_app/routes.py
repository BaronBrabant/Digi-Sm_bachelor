from my_app import app
from model import *
from flask import render_template, redirect, url_for, request

@app.route('/', methods=['GET', 'POST'])
def show_tasks():
    if request.method == 'POST':

        _task = request.form['task']
        _id = request.form['id']


        notOnlySpaceTask = False
        for characters in _task:
            if characters != ' ':
                notOnlySpaceTask = True
                
        notOnlySpaceID = False
        for characters in _id:
            if characters != ' ':
                notOnlySpaceID = True
        
        if _task and notOnlySpaceTask and notOnlySpaceID:
            toDo_dict[_id.replace(' ', '')] = _task
            return render_template('index.html', nb_task=len(toDo_dict), tasks=toDo_dict, valid = notOnlySpaceTask)
        elif _task and (not notOnlySpaceTask or not notOnlySpaceID):
            return render_template('index.html', nb_task=len(toDo_dict), tasks=toDo_dict, valid = (notOnlySpaceTask and notOnlySpaceID))
        else:
            return 'Problem with new task', 400
    else:
        return render_template ('index.html', nb_task=len(toDo_dict), tasks=toDo_dict)

@app.route("/delete/<string:key>")
def delete(key):
    toDo_dict.pop(key)
    return redirect('/', code=302)