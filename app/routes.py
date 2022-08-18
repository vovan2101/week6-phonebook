from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import PhoneBook, CreateAddress
from app.models import User, Contact


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/phonebook', methods=["GET", "POST"])
def phonebook():
    form = PhoneBook()
    if form.validate_on_submit():
        address = form.address.data
        name = form.name.data
        phone_number = form.phone_number.data
        new_user = User(address = address, name = name, phone_number = phone_number)
        print(f"{new_user.name} has been created.")
        return redirect(url_for('index'))      
    return render_template('phonebook.html', form = form)

@app.route('/createaddress', methods = ['GET','POST'])
def createaddress():
    form = CreateAddress()
    if form.validate_on_submit():
        phone_number = form.phone_number.data
        name = form.name.data
        new_contact = Contact(phone_number=phone_number, name=name)
        flash(f"{new_contact.phone_number} was added into your Phonebook", 'success')
    return render_template('createaddress.html', form=form)