from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return "<h1>Welcome to homepage.</h>"

@views.route('/login')
def login():
    return render_template("login.html")

