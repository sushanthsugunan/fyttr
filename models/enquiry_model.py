from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Enquiry(db.Model):
    __tablename__ = 'enquiries'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10))
    phone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(100))
    fitness_goal = db.Column(db.String(50), nullable=False)
    current_activity_level = db.Column(db.String(20))
    preferred_training = db.Column(db.String(20))
    message = db.Column(db.Text)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='Pending')

    def __repr__(self):
        return f'<Enquiry {self.name}, Goal: {self.fitness_goal}>'