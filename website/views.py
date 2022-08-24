import os
import sqlite3
from xmlrpc.client import boolean
import PyPDF2
from flask import Flask,flash, Blueprint, render_template, request,url_for,redirect,session
from sqlalchemy import true

from website.models import User
from . import db
from werkzeug.utils import secure_filename

currentlocation = os.path.dirname(os.path.abspath(__file__))

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

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        sqlconnection = sqlite3.Connection(currentlocation + "\database.db")
        cursor = sqlconnection.cursor()
        query1 = "SELECT email, password FROM User Where email = '"+email+"'AND password = '"+password+"'".format(email=email, password = password)

        rows = cursor.execute(query1)
        rows = rows.fetchall()
        if len(rows)==0:
            flash('Invalid username or password', category ='error')
        else:
            return redirect("/")
    return render_template("login.html")
   

@views.route("/ResetPass",  methods=['GET', 'POST'])
def reset_pass():

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        sqlconnection = sqlite3.Connection(currentlocation + "\database.db")
        cursor = sqlconnection.cursor()
        query1 = "UPDATE User SET password = '"+password+"' WHERE email='"+email+"'".format(email = email,password=password)
        cursor.execute(query1)
        sqlconnection.commit()
        return redirect("/login")
    return render_template("ResetPass.html")



@views.route("/SignUp" , methods=['GET', 'POST'])
def SignUp():
    if request.method == 'POST':
        first_name = request.form.get ('first_name')
        last_name = request.form.get ('last_name')
        email = request.form.get ('email')
        phone_number = request.form.get ('phone_number')
        password = request.form.get ('password')
        occupation = request.form.get ('occupation')
        date_of_birth = request.form.get ('date_of_birth')
        gender = request.form.get('gender')

        if len(first_name) < 2:
            flash('First name must be greater than 1 character.' , category ='error')
        elif len(last_name) < 2:
            flash('Last name must be greater than 1 character.' , category ='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.' , category ='error')
        elif len(phone_number) < 11:
            flash('Phone number must be eleven digits.' , category ='error')
        elif len(password) < 7:
            flash('Password must be atleast 7 characters' , category ='error')

        elif len(occupation) < 6:
            flash('Password must be atleast 6 characters' , category ='error')
       
        else:
            flash('Account created', category= 'success')
            pass
            
        sqlconnection =sqlite3.Connection(currentlocation + "\database.db")
        cursor = sqlconnection.cursor()
        query1 = "INSERT INTO User VALUES('{id}','{first_name}','{last_name}','{email}','{phone_number}','{password}','{occupation}','{date_of_birth}','{gender}')".format (id = 7, first_name = first_name, last_name = last_name, email = email, phone_number = phone_number, password = password, occupation = occupation, date_of_birth = date_of_birth, gender = gender)
        cursor.execute(query1)
        sqlconnection.commit()
        return redirect("/")
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

@views.route("/baseHome")
def baseHome():
    return render_template("baseHome.html")

@views.route('/details/<int:id>')
def RetrieveSingleEmployee(id):
    customer = User.query.filter_by(id=id).first()
    if customer:
        return render_template('userdetails.html', customer = customer)
    return f"Employee with id ={id} Doenst exist"