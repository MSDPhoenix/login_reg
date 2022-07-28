from login_app import app
from flask import render_template,redirect,request,session,flash
from login_app.models.user import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success/')
def success():
    if session['user']:
        return render_template('success.html')
    return redirect('/')

@app.route('/register/',methods=['POST'])
def register():
    if not User.validate_register(request.form):
        return redirect('/')
    session['user'] = User(request.form)
    return redirect('/success/')

@app.route('/login/',methods=['POST'])
def login():
    if not User.validate_login(request.form):
        return redirect('/')
    session['user'] = User(request.form)
    return redirect('/success/')

