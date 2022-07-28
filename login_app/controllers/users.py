from login_app import app
from flask import render_template,redirect,request,session,flash
from login_app.models.user import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success/')
def success():
    
    return render_template('success.html')

@app.route('/register/',methods=['POST'])
def register():

    return redirect('/success/')

@app.route('/login/',methods=['POST'])
def login():

    return redirect('/success/')

