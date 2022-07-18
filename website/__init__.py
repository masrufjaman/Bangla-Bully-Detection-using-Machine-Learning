import os
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'bangla bully detection using machine learning'
    ALLOWED_EXTS = {"txt", "pdf", "doc"}
    def check_file(file):
        return '.' in file and file.rsplit('.',1)[1].lower() in ALLOWED_EXTS
        
    from .admin import admin
    from .views import views

    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(views, url_prefix='/')

    return app