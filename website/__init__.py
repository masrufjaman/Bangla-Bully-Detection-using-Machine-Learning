from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "bangla bully detection using machine learning"
    # for database
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@127.0.0.1/snooper"
    db.init_app(app)
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    from .admin import admin
    from .views import views

    app.register_blueprint(admin, url_prefix="/admin")
    app.register_blueprint(views, url_prefix="/")

    return app
