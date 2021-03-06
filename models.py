"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

def connect_db(app):
  """Connect to database."""

  db.app = app
  db.init_app(app)

class User(db.Model):
  """ User."""

  __tablename__ = "users"

  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  first_name = db.Column(db.String(50), nullable = False)
  last_name = db.Column(db.String(50), nullable = False)
  image_url = db.Column(db.String(), nullable = False)

  posts= db.relationship("Post", backref = "user")

# suggested default URL: https://giphy.com/embed/l0Ex7SHlSIDcmYbBu


class Post(db.Model):
  """ Post."""

  __tablename__ = "posts"

  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  title = db.Column(db.Text, nullable = False)
  content = db.Column(db.Text, nullable = False)
  created_at = db.Column(db.DateTime, nullable = False, default = datetime.now())
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)

  # do representative 

class Tag(db.Model):
  """ Tag."""

  __tablename__ = "tags"

  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  name = db.Column(db.String(10), nullable = False)
  
  posts= db.relationship("Post", secondary="posttags", backref = "tag")

class PostTag(db.Model):
  """Post-Tag linking table"""

  __tablename__ = "posttags"

  post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), primary_key = True)
  tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"), primary_key = True)

