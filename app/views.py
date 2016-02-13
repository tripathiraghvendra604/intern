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
        return redirect ('/list')
    else:
        print 'Error Here'

    return render_template('form.html', form = form)

@app.route('/list', methods=['GET', 'POST'])
def user_data():
    datas = User.query.all()
    data = []
    for d in datas:
        data.append((d, d.id))
    return render_template('data.html', data=data, id=id)

@app.route('/delete/<id>')
def delete(id):
    print id
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/list')