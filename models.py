from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique = True) 
    phone = db.Column(db.String(20), nullable= False)
    email = db.Column(db.String(200))
    address = db.Column(db.String(200))
