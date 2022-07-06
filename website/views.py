from ast import Return
from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return "<h1>Welcome to homepage.</h>"

@views.route('/help')
def help():
    # return "<h1>Welcome to help page.</h>"
    return render_template("help.html")
    
@views.route('/message')
def message():
   return render_template("message.html")
@views.route('/upload')
def upload():
    return render_template("upload.html")
@views.route('/guidence')
def guidence():
    return render_template("guidence.html")
  
