from xml.etree.ElementTree import register_namespace
from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/phonebook')
def phonebook():
    return render_template('phonebook.html')