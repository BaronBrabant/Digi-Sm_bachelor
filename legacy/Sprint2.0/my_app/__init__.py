from flask import Flask, session
from flask_session import Session
from config import DevelopmentConfig, ProductionConfig
import os, sys
from pathlib import Path


sys.path.append(os.path.join(os.path.dirname(__file__), "."))
STATIC_DIR = os.path.abspath('my_app/static')
#MAIN_DIR = os.path.abspath('')
app = Flask (__name__, static_folder=STATIC_DIR)
app.config.from_object(ProductionConfig)



from .login_manager import login_manager
from .models import *

#app.register_blueprint(users_routes)

with app.app_context():
    db.drop_all()
    db.create_all()
    
    createUserTaskInit()


from .routes import *