from flask import Blueprint, render_template, redirect, url_for, flash
from chatapp.forms import RegistrationForm, LoginForm
from chatapp.models import User
from chatapp.extensions import db, bcrypt
from flask_login import login_user
from flask_login import logout_user
from flask import redirect, url_for





main = Blueprint('main', __name__)

# Use 'main' Blueprint for all routes
@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('main.login'))  # Ensure this refers to a view function within 'main' Blueprint
    return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Query the database for the user
        user = User.query.filter_by(email=form.email.data).first()
        # Check if the user exists and the password is correct
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)  # Log in the user
            flash('You have been logged in successfully!', 'success')
            return redirect(url_for('main.home'))  # Redirect to the home page after login
        else:
            flash('Login unsuccessful. Please check your email and password.', 'danger')
    return render_template('login.html', form=form)



@main.route('/logout')
def logout():
    logout_user()  # Log out the user
    return redirect(url_for('main.home'))  # Redirect to the home page after logout
