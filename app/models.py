from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash



class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    address = db.Column(db.String(50), nullable = False)
    name = db.Column(db.String(50), nullable = False)
    phone_number = db.Column(db.Integer, nullable = False, unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    #     self.password = generate_password_hash(kwargs['password'])
        db.session.add(self)
        db.session.commit()
