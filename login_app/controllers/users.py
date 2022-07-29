from login_app import app
from flask import render_template,redirect,request,session,flash
from login_app.models.user import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success/')
def success():
    if session['user_id']:
        user=User.get_by_id({'id':session['user_id']})
        return render_template('success.html',user=user)
    return redirect('/')

@app.route('/register/',methods=['POST'])
def register():
    if not User.validate_register(request.form):
        session['first_name']=request.form['first_name']
        session['last_name']=request.form['last_name']
        session['email']=request.form['email']
        session['password']=request.form['password']
        session['confirm_password]']=request.form['confirm_password']
        return redirect('/')
    session.clear()
    session['user_id'] = User.save(request.form)
    return redirect('/success/')

@app.route('/login/',methods=['POST'])
def login():
    if not User.validate_login(request.form):
        return redirect('/')
    session['user'] = User(request.form)
    return redirect('/success/')

