from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Contact(db.Model):
    id = db.Column(db.integer, primary_key=True)
    name = db.Column(db.string(20), nullable=False)
    phone = db.Column(db.string(20), nullable= False)
    email = db.Column(db.string(200))
    address = db.Column(db.string(200))
    