from login_app import app
from flask import render_template,redirect,request,session,flash
from login_app.models.user import User,bcrypt

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success/')
def success():
    if 'user_id' in session:
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
    password_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : password_hash
    }
    session['user_id'] = User.save(data)
    return redirect('/success/')

@app.route('/login/',methods=['POST'])
def login():
    if not User.validate_login(request.form):
        session['email']=request.form['email']
        session['password']=request.form['password']
        return redirect('/')
    session.clear()
    session['user_id'] = User.get_by_email(request.form).id
    return redirect('/success/')

@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')
