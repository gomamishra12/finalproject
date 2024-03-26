# auth_routes.py
from flask import Blueprint, render_template, redirect, url_for, flash
from ChatApp.forms import RegistrationForm, LoginForm
from ChatApp.models import User
from ChatApp import db, bcrypt

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    # Registration route logic

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # Login route logic

@auth.route('/logout')
def logout():
    # Logout route logic
