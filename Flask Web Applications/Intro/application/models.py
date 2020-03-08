from application import db
import datetime

class User(db.Document):
    user_id = db.IntField(unique = True)
    username = db.StringField(unique=True, max_length=50)
    password = db.StringField()
    email = db.StringField(unique=True, max_length=50)

class Userspost(db.Document):
    comment_id = db.IntField(unique=True)
    user_comment = db.StringField()
    date_created = db.DateTimeField(default=datetime.datetime.utcnow)