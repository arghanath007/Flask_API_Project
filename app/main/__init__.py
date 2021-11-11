from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from app.main.config import config_by_name

db=SQLAlchemy() #Creating the Database
flask_bcrypt=Bcrypt() #For encrypting the Database.

def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)  #To connect the app with the Database
    flask_bcrypt.init_app(app)

    return app
