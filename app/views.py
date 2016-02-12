from app import app
from flask import render_template, redirect
from .forms import UserForm
from .models import User
from app import db

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UserForm()

    if form.validate_on_submit():
        user = User(
            name = form.name.data,
            email = form.email.data,
            contact = form.contact.data,
            city = form.city.data,
            company = form.company.data,
            )
        db.session.add(user)
        db.session.commit()

        print 'Data Saved'
        return ('/list')
    else:
        print 'Error Here'

    return render_template('form.html', form = form)

@app.route('/list', methods=['GET', 'POST'])
def user_data():
    data = User.query.all()
    return render_template('data.html', data=data)
