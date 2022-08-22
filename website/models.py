from asyncio.windows_events import NULL
from enum import unique
from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,autoincrement = True, primary_key = True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(150),unique = True)
    phone_number = db.Column(db.String(11))
    password = db.Column(db.String(8))
    occupation = db.Column(db.String(10))
    date_of_birth =db.Column(db.Date)
   
