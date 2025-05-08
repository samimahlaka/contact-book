from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField
from wtforms.validators import DataRequired


class contactForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(message='Please enter name')],render_kw={'class' : 'input_box'})
    phone = StringField('phone', validators=[DataRequired(message='Please enter phone number')],render_kw={'class' : 'input_box'})
    email = StringField('email',render_kw={'class' : 'input_box'})
    address = StringField('address',render_kw={'class' : 'input_box'})
    submit =SubmitField('Submit')