from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm, PhoneBook, LoginForm
from app.models import User, Contact
from flask_login import login_user, logout_user, login_required, current_user



@app.route('/')
def index():
    contacts=[]
    if current_user.is_authenticated:
        contacts = current_user.contacts.all()
    return render_template('index.html', contacts=contacts)


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
@login_required
def phonebook():
    form = PhoneBook()
    if form.validate_on_submit():
        phone_number = form.phone_number.data
        name = form.name.data
        notes = form.notes.data
        new_contact = Contact(phone_number=phone_number, name=name, notes=notes, user_id = current_user.id)
        flash(f"{new_contact.name} was added into your Phonebook", 'success')
        return redirect(url_for('index'))
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

@app.route('/logout')
def logout():
    logout_user()
    flash("You have successfully logged out.", 'primary')
    return redirect(url_for("index"))

@app.route('/phonebook/<contact_id>')
@login_required
def view_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    return render_template('book.html', contact=contact)


@app.route('/phonebook/<contact_id>/edit', methods=["GET", "POST"])
@login_required
def edit_contact(contact_id):
    contact_to_edit = Contact.query.get_or_404(contact_id)
    if contact_to_edit.author != current_user:
        flash("You do not have permission to edit this phonebook", 'danger')
        return redirect(url_for('view_contact', contact_id=contact_id))
    form = PhoneBook()
    if form.validate_on_submit():
        name= form.name.data
        phone_number= form.phone_number.data
        notes= form.notes.data
        contact_to_edit.update(name=name, phone_number=phone_number, notes=notes)
        flash(f'{contact_to_edit.name} has been updated', 'success')
        return redirect(url_for('view_contact', contact_id=contact_id))
    return render_template('edit_contact.html')

@app.route('/phonebook/<contact_id>/delete')
@login_required
def delete_contact(contact_id):
    contact_to_delete = Contact.query.get_or_404(contact_id)
    if contact_to_delete.author != current_user:
        flash('You do not have permission to delete this contact', 'danger')
        return redirect(url_for('index'))
    contact_to_delete.delete()
    flash(f"{contact_to_delete.name} has been deleted", 'info')
    return redirect(url_for('index'))