from flask import render_template,request
from app import app
from app.forms import RegisterForm

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login')
def login():
    form = RegisterForm()
    return render_template("login.html", form=form)

@app.route('/register',methods = ['GET','POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        user = form.username.data
        print(user)

    return render_template("register.html",form=form)