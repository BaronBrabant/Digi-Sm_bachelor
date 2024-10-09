from sqlite3 import Date
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, IntegerField
from wtforms.validators import Length, InputRequired, ValidationError
from .models import *

name_validators = [InputRequired(), Length(min=3, max=30)]
passwd_validators = [InputRequired(), Length(min=6)]

# OK
class RegisterForm(FlaskForm):
    
    username = StringField(label='Username', validators=name_validators)
    passwd = PasswordField(label='Password', validators=passwd_validators)
    passwd_confirm = PasswordField(label='Confirm password')
    name = StringField(label='Name')
    firstname = StringField(label='First Name')
    group = StringField(label='Group')
    submit = SubmitField(label='Register')
    
    def validate_username(self, field):
        if field.data in [x.username for x in User.query.all()]:
            raise ValidationError('Username already taken')
        
    def validate_passwd(self, field):
        if self.passwd.data != self.passwd_confirm.data:
            raise ValidationError('Wrong password confirmation.')

# OK
class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=name_validators)
    passwd = PasswordField(label='Password', validators=passwd_validators)
    submit = SubmitField(label='Log-in')
    


# due -> date ok?
class TaskForm(FlaskForm):
    name = StringField(label='Taskname',
                       validators=[InputRequired(message="Enter a taskname."),
                                   Length(min=3, message="Taskname must be a least 3 characters long.")])
    description = StringField(label='Description')
    pokerScore = IntegerField(label = 'Poker score')
    due = DateField(label='Due', format='%Y-%m-%d')
    submit = SubmitField(label='Save')


class ProjectForm(FlaskForm):

    name = StringField(label='Projectname',
                       validators=[InputRequired(message="Enter a projectname."),
                                   Length(min=3, message="Projectname must be a least 3 characters long.")])
    description = StringField(label='Description')
    submit = SubmitField(label='Save')
    
class AddUserToProject(FlaskForm):
    
    username = StringField(label='Username', validators=name_validators)
    submit = SubmitField(label='Add user to project')
    