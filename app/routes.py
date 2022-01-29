from dataclasses import field
from flask import render_template, request,redirect, flash, url_for
from app import app
from app.forms import RegisterForm, LoginForm
from app import db
from app.database import User
from flask_login import login_user, logout_user


@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == "POST":
        skill = request.form.get("skill")
        people = User.query.filter_by(field = skill).all()
        return render_template("home.html",people=people)
    else:
        people=[]
        return render_template("home.html",people=people)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        attempt_user = User.query.filter_by(username=form.username.data).first()
        if attempt_user and form.password.data == attempt_user.password:
            login_user(attempt_user)
            flash("Success!!")
            return redirect(url_for('profile',id=attempt_user.id))

        else:
            flash("Invalid Username or Password")

    return render_template("login.html", form=form)


@app.route('/register',methods = ['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username = form.username.data,
                    password = form.password.data,
                    name = form.name.data,
                    email = form.email.data ,
                    phno = form.phone.data, 
                    education_status = form.education.data ,
                    field = form.field.data ,
                    projects = form.project.data )
        try:
            db.session.add(user)
            db.session.commit()
            return redirect('/')
        except:
            return "Error adding to database"
    if form.errors != {}:
        for msg in form.errors.values():
            flash(f'Error: {msg}')
    return render_template("register.html",form=form)


@app.route('/profile/<int:id>')
def profile(id):
    user = User.query.get(id)
    return render_template("profile.html",user=user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("home"))