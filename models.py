from app import db

#import from models, in terminal to create database file
class Task(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    date=db.Column(db.Date,nullable=False)

#all the columns that we need in a task data model

def __repr__(self): #function which is going to represent each instance
    return f'{self.title}'



