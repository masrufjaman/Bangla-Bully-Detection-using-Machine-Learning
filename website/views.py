import os
from xmlrpc.client import boolean
import PyPDF2
from flask import Flask,flash, Blueprint, render_template, request,url_for,redirect,session
from sqlalchemy import true
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
       a = PyPDF2.PdfFileReader('Application form Amabassador programme.pdf')
       str = ""
       for i in range(1,10):
         str += a.getPage(i).extract_text()
       with open ("text.txt", "w") as f:
         f.write(str)
       file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
       print("File saved")

 return render_template("homepage.html")
    
   
@views.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@views.route("/ResetPass")
def reset_pass():
    return render_template("ResetPass.html")


@views.route("/SignUp" , methods=['GET', 'POST'])
def SignUp():
    if request.method == 'POST':
        fname = request.form.get ('fname')
        lname = request.form.get ('lname')
        email = request.form.get ('email')
        psw = request.form.get ('psw')
        occupation = request.form.get ('occupation')
        dob = request.form.get ('dob')

        if len(fname) < 2:
            flash('First name must be greater than 1 character.' , category ='error')
        elif len(lname) < 2:
            flash('Last name must be greater than 1 character.' , category ='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.' , category ='error')
        elif len(psw) < 7:
            flash('Password must be atleast 7 characters' , category ='error')
        
        elif len(occupation) < 6:
            flash('Password must be atleast 6 characters' , category ='error')


        else:
            flash('Account created', category= 'success')
            pass

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
@views.route("/start")
def start():
    return render_template("start.html")
@views.route("/footer")
def footer():
    return render_template("footer.html")
@views.route("/userprofile")
def userprofile():
    return render_template("userprofile.html")