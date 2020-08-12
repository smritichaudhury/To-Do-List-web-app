from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)#creates your flask app;instastiation
app.config['SECRET_KEY']='smriti' #for forms in csrf_Token. you need a secret key
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db' #url for sql db and name of the file is data

db=SQLAlchemy(app)
# we have a db instance but we also need a data model.
from routes import *



if __name__=='__main__':
    app.run(debug=True) #gives debug functionality from flask