from my_app import app
from my_app.model import *
from flask import render_template, redirect, request, url_for
from flask_login import login_user, logout_user, login_required, current_user
from .forms import RegisterForm, LoginForm, TaskForm
from .login_manager import *


def nbTask():
    print(current_user.username)
    nb_toDo = Task.query.filter_by(user_id=current_user.id).count()

    return nb_toDo


def nbRemainingTask():
    print(current_user.username)
    nb_toDo = Task.query.filter_by(user_id=current_user.id, done=False).count()

    return nb_toDo


# -------------
@app.route('/', methods=['GET', 'POST'])
@login_required
def show_tasks():
    toDo_list = Task.query.filter_by(user_id=current_user.username)
    nb_tot = nbTask()
    nb_toDo = nbRemainingTask()
    
    return render_template('toDoList.html', toDo_list=current_user.tasks, nb_tot=nb_tot, nb_toDo=nb_toDo, admin=current_user.group)

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
@app.route("/modify_username/<string:str>", methods = ['GET', 'POST'])
@login_required
def modify_username(str):
    user_info = User.query.filter_by(username=current_user.username).first()
    user_info.username = str
    return redirect(url_for('show_profile'))

@app.route("/modify_name/<string:str>", methods = ['GET', 'POST'])
@login_required
def modify_name(str):
    user_info = User.query.filter_by(username=current_user.username).first()
    user_info.name = str
    return redirect(url_for('show_profile'))

@app.route("/modify_firstname/<string:str>", methods = ['GET', 'POST'])
@login_required
def modify_firstname(str):
    user_info = User.query.filter_by(username=current_user.username).first()
    user_info.firstname = str
    return redirect(url_for('show_profile'))
    """


@app.route('/admin', methods=['GET', 'POST'])
@login_required
def show_users():
    if current_user.group == True:
        nb_tot = nbTask()
        nb_toDo = nbRemainingTask()
        userList = User.query.all()
        return render_template('admin.html', toDo_list=current_user.tasks, nb_tot=nb_tot, nb_toDo=nb_toDo, admin=current_user.group, user_list = userList )

# -------------------
@app.route("/newTask", methods=['GET', 'POST']) 
@login_required 
def newTask():
    form = TaskForm()
    if request.method == 'POST':


        _date = request.form ["time-date"]
        due = _date[8:10] +"/" +  _date[5:7] +"/" +  _date[0:4]
        
        new_task = Task(name=form.name.data, description=form.description.data, due=due,
                        done=False, user=current_user)
    
        db.session.add(new_task)
        db.session.commit()
            
        return redirect('/', code=302)
    else:
        return render_template('newTask.html', admin=current_user.group)

# -----------
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
@app.route("/check_uncheck/<int:task_id>")
@login_required
def check_uncheck(task_id):
    task = Task.query.filter_by(id=task_id).first()
    
    if task is None or task.user != current_user:
        return render_template('error.html', status=404, message="Cannot check/uncheck this task (task not found).")
    else:  
        task.done = not task.done
        db.session.commit()
        return redirect('/', code=302)
    
# -------------
@app.route("/modify/<int:task_id>", methods=['GET', 'POST'])
@login_required
def modal(task_id):
    task = Task.query.filter_by(id=task_id).first()
    
    if task is None or task.user != current_user:
        return render_template('error.html', status=404, message="Cannot modify this task (task not found).")
    else:
        form = TaskForm()
        if request.method == 'POST':
            
            _date = request.form ["time-date"]
            due = _date[8:10] +"/" +  _date[5:7] +"/" +  _date[0:4]
            
            task.name = form.name.data
            task.description = form.description.data
            task.due = due
            db.session.commit()
            
            return redirect('/', code=302)
        else:
            toDo_list = Task.query.filter_by(user_id=current_user.username)
            nb_toDo = nbRemainingTask()
            return render_template('modify.html', nameTask=task.name, nameDescr=task.description, toDo_list=current_user.tasks, nb_tot=toDo_list.count(), nb_toDo=nb_toDo, admin=current_user.group, task_id=task_id)
    


# -------------
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



# -------------- Registration & Log --------------

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    
    if request.method == 'GET':
        return render_template('register.html', form=form, user=current_user)
    if not form.validate_on_submit():
        return render_template('register.html', form=form, user=current_user)

    _date = request.form ["time-date"]

    birthdate = _date[8:10] +"/" + _date[5:7] +"/" + _date[0:4]
    
    new_user = createUser(form.username.data, form.name.data, form.firstname.data, birthdate, form.passwd.data)

    #new_user.set_password(form.passwd.data)
    db.session.add(new_user)
    db.session.commit()
    
    login_user(new_user, remember=True, force=True)
    
    return redirect(url_for('show_tasks'))

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
            return redirect(url_for('show_tasks'))
    
    return render_template('error.html', status = 403, message='You have been blocked by the admin.')

# OK
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('show_tasks'))

