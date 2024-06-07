from datetime import datetime, timezone

from flask import Blueprint, login_required, render_template, flash, redirect, url_for
from flask_login import current_user, login_required, login_user, logout_user

from .forms import LoginForm, RegistrationForm

from app.models import User

from app import db

auth = Blueprint('auth', __name__)


# login
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        # return to index page if already logged in
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        # query table to look up username which was submitted in the form and see if it exists
        user = User.query.filter_by(username=form.username.data).first()
        # if the user exists
        if user:
            # check the hash
            # compare what's already in the database with what the user just typed into the form
            if user.check_password(form.password.data):
                # log them in
                login_user(user, remember=form.remember_me.data)
                flash("Login successful")
                return redirect(url_for('index'))
            else:
                flash("Wrong password, try again")
                return redirect(url_for('login'))
        else:
            flash("That user does not exist")

    return render_template('login.html',
                           title='Log In',
                           form=form)


# logout
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out")
    return redirect(url_for('index'))


# register an account
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        # return to index page if already logged in
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    email=form.email.data,
                    date_joined=datetime.now(timezone.utc))
        user.set_password(form.password_hash.data)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created")
        return redirect(url_for('login'))

    return render_template('register.html',
                           title='Register',
                           form=form)