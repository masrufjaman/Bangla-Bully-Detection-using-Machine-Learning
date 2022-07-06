from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("homepage.html")

@views.route('/login')
def login():
    return render_template("login.html")

@views.route('/ResetPass')
def reset_pass():
    return render_template("ResetPass.html")

@views.route('/SignUp')
def SignUp():
    return render_template("SignUp.html")

@views.route('/help')
def help():
    # return "<h1>Welcome to help page.</h>"
    return render_template("help.html")
    #<--- after you create an html page for help webpage

@views.route('/profile')
def profile():
    # return "<h1>Welcome to profile page.</h>"
    return render_template("profile.html")