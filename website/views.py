from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return "<h1>Welcome to homepage.</h>"

@views.route('/login')
def login():
    return render_template("login.html")

@views.route('/ResetPass')
def ResetPass():
    return render_template("ResetPass.html")

@views.route('/SignUp')
def SignUp():
    return render_template("SignUp.html")

