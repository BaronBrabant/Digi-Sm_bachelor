from my_app import app
from model import *
from flask import render_template, redirect, request


def nbRemainingTask():
    nb = 0
    for key in toDo_dict:
        if toDo_dict[key][1] == False:
            nb = nb + 1
    return nb

@app.route('/', methods=['GET', 'POST'])
def show_tasks():
    return render_template('index.html')
    
@app.route("/newTask", methods=['GET', 'POST'])  
def newTask():
    if request.method == 'POST':

        _id = request.form['id']
        _task = request.form['task']
        
        validID = False
        for characters in _id:
            if characters != ' ':
                validID = True

        validTask = False
        for characters in _task:
            if characters != ' ':
                validTask = True
                
        if validID and validTask:
            toDo_dict[_id.replace(' ', '')] = [_task, False]
            return redirect('/', code=302)
        else:
            return render_template('newTask.html', validID=validID, validTask=validTask)
    else:
        return render_template('newTask.html', validID=True, validTask=True)
    

@app.route("/delete/<string:key>")
def delete(key):
    toDo_dict.pop(key)
    return redirect('/', code=302)

@app.route("/check_uncheck/<string:key>")
def check_uncheck(key):
    toDo_dict[key][1] = not toDo_dict[key][1]
    return redirect('/', code=302)

@app.route("/modify/<string:key>", methods=['GET', 'POST'])
def modal(key):
    if request.method == 'POST':

        _task = request.form['task']

        validTask = False
        for characters in _task:
            if characters != ' ':
                validTask = True
        
        if validTask:
            toDo_dict[key] = [_task, False]
            return redirect('/', code=302)
        else:
            return redirect('/', code=302)
    else:
        return render_template ('modify.html', key=key, task=toDo_dict[key][0], tasks=toDo_dict, nb_tot=len(toDo_dict), nb_toDo=nbRemainingTask())
    

    