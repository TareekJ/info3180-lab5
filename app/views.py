import os
from app import db,app,allowed_exts
from flask import render_template, request, redirect, url_for, flash
from .models import UserProfile
from .forms import NewForm
from werkzeug.utils import secure_filename
import datetime
from sqlalchemy import exc



###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')
    
@app.route('/profile', methods=['POST','GET'])
def profile():
    newProfileForm = NewForm()
    
    if request.method == 'POST':
        if newProfileForm.validate_on_submit()==True:
            try:
            
                firstname = newProfileForm.firstname.data
                lastname = newProfileForm.lastname.data
                gender = newProfileForm.gender.data
                email = newProfileForm.email.data
                location = newProfileForm.location.data
                bio = newProfileForm.bio.data
                created = str(datetime.datetime.now()).split()[0]
                
                photo = newProfileForm.photo.data
                photo_name = secure_filename(photo.filename)
               
                user = UserProfile(firstname,lastname,gender,email,location, bio, created, photo_name)
                
                db.session.add(user)
                db.session.commit()
                
                photo.save(os.path.join(app.config['UPLOAD_FOLDER'],photo_name))
                flash('Successfullly added.', 'success')
                return redirect(url_for('profiles'))
            
            except Exception as e:
                db.session.rollback()
                flash("Internal Error", "danger")
                return render_template("create_profile.html", newProfileForm = newProfileForm)
                
        errors = form_errors(newProfileForm)
        flash(''.join(error+" " for error in errors),"danger")
        
    return render_template("create_profile.html", newProfileForm = newProfileForm)
    
    




########################################################################################



@app.route('/profiles', methods=['GET','POST'])
def profiles():
    
    profiles= UserProfile.query.all()
    profile=[]
    
    for user in profiles:
        profile.append({"pro_pic": user.photo, "f_name":user.firstname, "l_name":user.lastname, "gender":user.gender, "location":user.location, "email":user.email, "bio":user.bio})
    
    return render_template('profiles.html', profile=profile)


#######################################################################################


@app.route('/profile/<userid>', methods=['GET', 'POST'])
def userprofile(userid):
    user = UserProfile.query.filter_by(id=userid).first()
    if user is None:
        return redirect(url_for('home'))
    
    c_y = int(user.created_on.split("-")[0])
    c_m = int(user.created_on.split("-")[1])
    c_d = int(user.created_on.split("-")[2])
    
    user.created_on = format_date_joined(c_y,c_m,c_d)
    
    return render_template('profile.html', user=user)
    
###
# The functions below should be applicable to all Flask apps.
###

def format_date_joined(yy,mm,dd):
    return datetime.date(yy,mm,dd).strftime("%8, %d, %Y")

def read_file(filename):
    data= " "
    
    with open(filename, "r") as stream:
        data = stream.read()
        
    return data

def form_errors(form):
    error_list=[]
    for field, errors in form.errors.items():
        for error in errors:
            error_list.append(field+": "+error)
    return error_list



@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")