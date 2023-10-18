from asyncio.windows_events import NULL
from datetime import timezone
from enum import unique
from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, db.Sequence('seq_reg_id', start=1, increment=1),primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(50),unique = True)
    phone_number = db.Column(db.String(11))
    password = db.Column(db.String(8))
    occupation = db.Column(db.String(10))
    date_of_birth =db.Column(db.Date)
    gender = db.Column(db.String(20))

class Message(db.Model):
    email = db.Column(db.String(50),primary_key = True)
    message = db.Column(db.String(300))
   