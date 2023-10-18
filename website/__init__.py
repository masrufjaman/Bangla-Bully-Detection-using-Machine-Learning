import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy ()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'bangla bully detection using machine learning'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
        
    from .admin import admin
    from .views import views

    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(views, url_prefix='/')

    from .models import User, Message
    

    create_database(app)

    return app

def create_database(app):
    if not path.exists ('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created database!')