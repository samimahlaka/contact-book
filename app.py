from flask import Flask, render_template, flash, redirect, request
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
        Name= form.name.data.strip().lower()
        existing = Contact.query.filter_by(name=Name).first()
        if existing:
            flash("A contact with this name already exist, please use another name")
            return redirect ('/add_contact')
        
        
        newContact = Contact(
            name = Name,
            phone = form.phone.data,
            email = form.email.data, 
            address = form.address.data
        )
        db.session.add(newContact)
        db.session.commit()
        
        flash('Contact added successfully')
        return redirect("/view_contacts")

    return render_template('add_contact.html',form=form)

@app.route('/view_contacts' , methods =['GET'])
def view_contacts():
        contacts=Contact.query.all()
        return render_template('view_contacts.html', contacts=contacts)
    

@app.route('/delete_contact', methods = ['GET', 'POST'])
def delete_contact():
    if request.method == 'POST':
        name = request.form.get('name')
        
        existing = Contact.query.filter_by(name=name.lower()).first()
        if existing:
            db.session.delete(existing)
            db.session.commit()
            
            flash(f'Contact "{name}" has been deleted successfully!')
            return redirect('/view_contacts')
        else:
            flash(f'No contact found with name "{name}".')
            return redirect('/delete_contact')
    
    return render_template("delete_contact.html")


@app.route('/update_contact/<int:id>', methods = 'POST')
def update_contact(id):
    form = contactForm
    if form.validate_on_submit:
        contact_update = Contact(
            name = form.name.data,
            phone = form.phone.data,
            email = form.email.data, 
            address = form.address.data
        )
        
        db.session.update()
        
    

        


if __name__ == '__main__':
    app.run(debug=True, port=5050)
