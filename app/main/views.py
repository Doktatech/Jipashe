from flask import Flask
from . import main
import datetime
from flask import render_template, request, redirect, url_for, abort, flash
from flask_login import login_required
from ..models import User, Post, Comment
from .forms import UpdateProfile, PostForm , CommentForm
from .. import db, photos
app = Flask(__name__)


# views
@main.route("/")
def index():
   '''
   title = "Jipashe News"
   '''
   title = 'Jipashe News'
   posts = Post.query.all()

   return render_template('index.html', title= title, posts = posts)
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    return render_template("profile/profile.html", user = user)