from flask_login import LoginManager
from . import app
from .models import User

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.login_message = 'You cannot access this page. Please log in to access this page.'
login_manager.session_protection = 'strong'


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()



