from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField
from wtforms.validators import DataRequired


class contactForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(message='Please enter name') ])
    phone = StringField('phone', validators=[DataRequired(message='Please enter phone number')])
    email = StringField('email')
    address = StringField('address')
    submit =SubmitField('Submit')