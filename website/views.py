# from crypt import methods
# from crypt import methods
from flask import Flask, Blueprint, render_template, request
from werkzeug.routing import Rule

views = Blueprint("views", __name__)


@views.route('/', method=['post','get'])
def home():
    return render_template("homepage.html")
    

@views.route("/login")
def login():
    return render_template("login.html")


@views.route("/ResetPass")
def reset_pass():
    return render_template("ResetPass.html")


@views.route("/SignUp")
def SignUp():
    return render_template("SignUp.html")


@views.route("/profile")
def profile():
    return render_template("profile.html")


@views.route("/help")
def help():
    return render_template("help.html")


@views.route("/message")
def message():
    return render_template("message.html")


@views.route("/upload")
def upload():
    return render_template("upload.html")


@views.route("/guidence")
def guidence():
    return render_template("guidence.html")