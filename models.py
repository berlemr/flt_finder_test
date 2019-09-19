#from app import db
# from db_util import db
# from app import app
# from flask_sqlalchemy import SQLAlchemy
#
# db = SQLAlchemy(app)

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # NOTE: app not imported from app.py and passed in


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(80), unique=True, nullable=False)

    @staticmethod
    def get_all_cities():
        return [i.city for i in Destination.query.all()]