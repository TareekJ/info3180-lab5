from flask import json, jsonify
from . import db

class UserProfile(db.Model):
	  __tablename__ = "user_profile"
	  id = db.Column(db.Integer, primary_key=True)
	  firstname 		= db.Column(db.String(80))
	  lastname 		    = db.Column(db.String(80))
	  gender			= db.Column(db.String(10))
	  email             = db.Column(db.String(80))
	  location          = db.Column(db.String(80))
	  bio 			    = db.Column(db.String(250))
	  created			= db.Column(db.DateTime())
	  photo				= db.Column(db.String(80))
	 
	 
def __init__(self,id,firstname,lastname,gender,email,location,bio,photo,created):
		self.id				= id
		self.firstname   	= firstname
		self.lastname 		= lastname
		self.gender 		= gender
		self.email 	    	= email
		self.location 		= location
		self.bio 			= bio
		self.photo          = photo
		self.created		= created
		
		
		
		
	
def is_authenticated(self):
        return True

def is_active(self):
        return True

def is_anonymous(self):
        return False

def get_id(self):
     try:
        return unicode(self.id)  # python 2 suppory
     except NameError:
        return str(self.id)  # python 3 support

def __repr__(self):
     return '<User %r>' % (self.first_name)			