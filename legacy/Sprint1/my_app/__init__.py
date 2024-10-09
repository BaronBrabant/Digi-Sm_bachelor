from flask import Flask
from config import DevelopmentConfig, ProductionConfig
import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), "."))
STATIC_DIR = os.path.abspath('my_app/static')
app = Flask (__name__, static_folder=STATIC_DIR)

app = Flask (__name__)
app.config.from_object(ProductionConfig)

from .login_manager import login_manager
from .model import *

#app.register_blueprint(users_routes)

with app.app_context():
    db.drop_all()
    db.create_all()

    createUserInit()
    
    


from .routes import *