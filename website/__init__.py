import os
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'bangla bully detection using machine learning'
    
    from .admin import admin

    app.register_blueprint(admin, url_prefix='/admin')

    return app