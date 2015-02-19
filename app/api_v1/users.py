from ..auth import auth_token
from . import api
from ..decorators import json
from ..forms import UserCreateForm
from .. import db
from ..models import User


@api.route('/users', methods=['POST'])
def new_user():
    print("vamos atomos")
    form = UserCreateForm()
    if not form.validate_on_submit():
        return form.errors, 422
    user = User(form.email.data, form.password.data)
    db.session.add(user)
    db.session.commit()
    return {}, 201


@api.route('/users', methods=['GET'])
@json
@auth_token.login_required
def get_users():
    users = User.query.all()
    # ESTA MAL, Y DEBERIA DE FILTRAR LO QUE VUELVO
    return {'users': [user for user in users]}


@api.route('/users/<int:id>', methods=['GET'])
@json
@auth_token.login_required
def get_user(id):
    user = User.query.get_or_404(id)
    return user


@api.route('/hola_mundo')
def hola_mundo():
    return("hola mundo2")
