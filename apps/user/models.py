from datetime import datetime

from exts import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(30))
    icon = db.Column(db.String(100))
    isdelete = db.Column(db.Boolean, default=False)
    rdatetime = db.Column(db.DateTime, default=datetime.now)

    def __str__(self):
        return self.username


class Message(db.Model):
    stu_card = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    stu_name = db.Column(db.String(15), nullable=False)
    college = db.Column(db.String(20), nullable=False)
    major = db.Column(db.String(20), nullable=False)
    t_lass = db.Column(db.String(20), nullable=False)
    course = db.Column(db.String(10), nullable=False)
    score = db.Column(db.String(10), nullable=False)

    def __str__(self):
        return self.stu_name



