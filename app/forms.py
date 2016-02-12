from flask.ext.wtf import Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Email

class UserForm(Form):
    name = StringField(validators = [DataRequired()])
    email = StringField(validators = [DataRequired(), Email()])
    contact = StringField(validators = [DataRequired()])
    city = StringField(validators = [DataRequired()])
    company = StringField(validators = [DataRequired()])