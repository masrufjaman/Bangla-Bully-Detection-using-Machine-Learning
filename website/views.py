from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return "<h1>Welcome to homepage.</h>"

@views.route('/profile')
def profile():
    return "<h1>Welcome to profile page.</h>"
    # return render_template("html_file_name.html")   <--- after you create an html page for user_profile webpage