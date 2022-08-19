from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm, Phonebook, LoginForm
from app.models import User, Contact
from flask_login import login_user, logout_user, login_required, current_user



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data
        existing_user = User.query.filter((User.email == email) | (User.username == username)).first()
        if existing_user: 
            flash('A user with that username or email already exist.', 'danger')
            return redirect(url_for('signup'))
        new_user = User(email=email, username=username, password=password)
        flash(f"{new_user.username} has been created.", "success")
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)


@app.route('/phonebook', methods = ['GET','POST'])
def phonebook():
    form = Phonebook()
    if form.validate_on_submit():
        phone_number = form.phone_number.data
        name = form.name.data
        notes = form.notes.data
        new_contact = Contact(phone_number=phone_number, name=name, notes=notes)
        flash(f"{new_contact.name} was added into your Phonebook", 'success')
    return render_template('phonebook.html', form=form)


@app.route('/login', methods = ["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username = username).first()
        if user is not None and user.check_password(password):
            login_user(user)
            flash(f'Welcome back {user.username}!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Incorrect username and/or password. Please try again', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html', form=form)