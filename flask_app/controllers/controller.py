from flask_app import app
from flask import render_template, request, redirect, session, flash
# from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/portfolio/enter')

@app.route('/portfolio/enter')
def enter():
    return render_template('index.html')

@app.route('/portfolio/home')
def home():
    return render_template('home.html')

@app.route('/portfolio/work')
def work():
    return render_template('work.html')

@app.route('/portfolio/contact')
def contact():
    return render_template('contact.html')