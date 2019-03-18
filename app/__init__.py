from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from subprocess import call


#configuartion uploads
app = Flask(__name__)
app.config['SECRET_KEY']= "SuperSecretKey"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:project1@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOAD_FOLDER']= './app/static/photo'
allowed_exts =["png","jpg","jpeg"]
db = SQLAlchemy(app)


from app import views
