import os
from flask import Flask,flash, Blueprint, render_template, request,url_for,redirect,session
from werkzeug.utils import secure_filename

views = Blueprint("views", __name__)

UPLOAD_FOLDER = './website/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@views.route('/', methods=['GET', 'POST'])
def home():
    
 if request.method == 'POST':
        # check if the post request has the file part
    if 'file' not in request.files:
       flash('No file part')
       return redirect(request.url)
    file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
    if file.filename == '':
       flash('No selected file')
       return redirect(request.url)
    if file and allowed_file(file.filename):
       filename = secure_filename(file.filename)
       file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
 return render_template("homepage.html", filename="filename")
   

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