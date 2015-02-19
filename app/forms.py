from flask.ext.wtf import Form

from wtforms_alchemy import model_form_factory
from wtforms import StringField
from wtforms.validators import DataRequired

from app import db
from .models import User

# Using WTForms-Alchemy with Flask-WTF:
# http://wtforms-alchemy.readthedocs.org/en/latest/advanced.html#using-wtforms-\alchemy-with-flask-wtf
# more documentation:
# http://wtforms-alchemy.readthedocs.org/en/latest/index.html

BaseModelForm = model_form_factory(Form)


class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session


class UserCreateForm(ModelForm):
    class Meta:
        model = User


class SessionCreateForm(Form):
    email = StringField('name', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
