from werkzeug import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy import DateTime
from . import db, login_manager



class User(UserMixin, db.Model()):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(225), nullable=False, unique=True, index=True)
    password_hash = db.Column(db.String(128))
    address = db.Column(db.String(300), nullable=False)
    created_on = db.Column(DateTime(), default=datetime.now)
    updated_on = db.Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
