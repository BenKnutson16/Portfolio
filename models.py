from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('Title', db.String())
    date = db.Column('Date', db.DateTime)
    description = db.Column('Description', db.String())
    skills = db.Column('Skills practiced', db.String())
    link = db.Column('GitHub link', db.String())

    def __repr__(self):
        return f"Project #{self.id}: {self.title}"
