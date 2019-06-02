from datetime import datetime
from . import db 
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,  primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True, index =True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

    posts = db.relationship('Post',backref='user',lazy='dynamic')
    comments = db.relationship('Comment', backref = 'comment', lazy= "dynamic")