from app import app
from flask import render_template
from app.forms import PhoneBook
from app.models import User


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
    return render_template('phonebook.html', form = form)