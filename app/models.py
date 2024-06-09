from . import db
from datetime import datetime

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    box_id = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
