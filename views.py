from flask import render_template, request, redirect, url_for
from .app import app,db
from .models import User
 

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            # login successful, redirect to user dashboard
            return redirect(url_for('dashboard', user_id=user.id))
        else:
            # login failed, show error message
            error_message = 'Invalid username or password'
            return render_template('login.html', error_message=error_message)
    else:
        return render_template('login.html')

# User dashboard
@app.route('/dashboard/<int:user_id>')
def dashboard(user_id):
    user = User.query.get(user_id)
    return render_template('dashboard.html', user=user)
 ##comment