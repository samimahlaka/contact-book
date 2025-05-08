from flask import Flask, render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from models import Contact, db
from forms import contactForm

app = Flask(__name__)

app.secret_key = 'dev25'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add_contact', methods = ['GET','POST'])
def add_contact():
    form = contactForm()

    if form.validate_on_submit():
        newContact = Contact(
            name = form.name.data,
            phone = form.phone.data,
            email = form.email.data, 
            address = form.address.data
        )
        db.session.add(newContact)
        db.session.commit()
        
        flash('Contact added successfully')
        return redirect("/view_contacts")

    return render_template('add_contact.html',form=form)






if __name__ == '__main__':
    app.run(debug=True)
