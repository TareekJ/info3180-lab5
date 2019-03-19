from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from subprocess import call


#configuartion uploads
app = Flask(__name__)
app.config['SECRET_KEY']= "SuperSecretKey"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://vdkjenptsrjwie:7c0806d7a96c62d7637a9993379f3f4155ba804ce0e59be0b83675791e29a7b9@ec2-54-221-236-144.compute-1.amazonaws.com:5432/d6dsm7o8b5ljn5"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:project1@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOAD_FOLDER']= './app/static/photo'
allowed_exts =["png","jpg","jpeg"]
db = SQLAlchemy(app)


from app import views
