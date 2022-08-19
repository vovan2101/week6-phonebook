from tabnanny import check
from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin




class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50), nullable = False, unique=True)
    username = db.Column(db.String(50), nullable = False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    date_created = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
    contacts = db.relationship('Contact', backref='author', lazy='dynamic')



    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_password = (kwargs['password'])
        db.session.add(self)
        db.session.commit()
    
    def check_password(self,password):
        return check_password_hash(self.password, password)

    def set_password(self, password):
        self.password = generate_password_hash(password)


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    phone_number = db.Column(db.String(50), nullable = False)
    name = db.Column(db.String(50), nullable = False)
    notes = db.Column(db.String(250))
    date_created = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()
