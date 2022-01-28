from flask import render_template, request,redirect, flash
from app import app
from app.forms import RegisterForm, LoginForm
from app import db
from app.database import User

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        user = User.query.get(form.username.data).first()
        if user and form.password.data == User.query.filter_by(username=form.username.data).first().password:
            flash("sucess")
        else:
            flash("failed")

    return render_template("login.html", form=form)

@app.route('/register',methods = ['GET','POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        user = User(username = form.username.data,
                    password = form.password.data,
                    name = form.name.data,
                    email = form.email.data ,
                    phno = form.phone.data, 
                    education_status = form.education.data ,
                    field = form.field.data ,
                    projects = form.project.data )
        db.session.add(user)
        db.session.commit()
        return redirect('/login')

    return render_template("register.html",form=form)