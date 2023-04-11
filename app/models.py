# Add any model classes for Flask-SQLAlchemy herefrom . import db
from datetime import datetime
from . import db
class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200))
    description = db.Column(db.Text())
    poster = db.Column(db.String())
    
    def __init__(self, title, description, poster):
        self.title = title
        self.description = description
        self.poster = poster

    def __repr__(self):
        return '<Movie %r>' % (self.title)