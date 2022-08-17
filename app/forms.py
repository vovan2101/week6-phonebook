from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length


class PhoneBook(FlaskForm):
    address = StringField('Address', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    phone_number = StringField('Phone number', validators=[DataRequired(), Length(min=7, max=14)])
    submit = SubmitField()
