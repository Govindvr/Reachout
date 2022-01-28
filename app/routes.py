from flask import render_template
from app import app
from app.forms import RegisterForm

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login')
def login():
    return "login page"

@app.route('/register')
def register():
    form = RegisterForm()
    return render_template("register.html",form=form)