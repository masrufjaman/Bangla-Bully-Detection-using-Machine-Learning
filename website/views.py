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
    #<--- after you create an html page for help webpage 