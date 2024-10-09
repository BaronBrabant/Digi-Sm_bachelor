from sqlite3 import Date
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, IntegerField, validators
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
        
        if " " in field.data:
            raise ValidationError('Username can not contain empty spaces')
        
        
    def validate_passwd(self, field):
        if self.passwd.data != self.passwd_confirm.data:
            raise ValidationError('Wrong password confirmation.')
        
        if " " in self.passwd.data:
            raise ValidationError('Password can not contain empty spaces')

# OK
class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=name_validators)
    passwd = PasswordField(label='Password', validators=passwd_validators)
    submit = SubmitField(label='Log-in')

    def validate_username(self, username):
        if username.data not in [x.username for x in User.query.all()]:
            raise ValidationError('Username does not exist.')

    def validate_passwd(self, passwd):
        hashed = db.session.query(User.passwd_hash).filter_by(username=self.username.data).first()

        if hashed is not None:
            if not check_password_hash(hashed[0], passwd.data):
                raise ValidationError('Wrong password.')
    


# due -> date ok?
class TaskForm(FlaskForm):
    name = StringField(label='Taskname',
                       validators=[InputRequired(message="Enter a taskname."),
                                   Length(min=3, message="Taskname must be a least 3 characters long.")])
    description = StringField(label='Description')
    pokerScore = IntegerField(label = 'Poker score')
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

class AddFriend(FlaskForm):
    
    username = StringField(label='Username', validators=name_validators)
    submit = SubmitField(label='Send Friend Request')
    