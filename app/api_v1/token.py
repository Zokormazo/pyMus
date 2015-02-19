# authentication token route
from ..auth import auth
from . import api
from flask import g
from ..decorators import json


@api.route('/get-auth-token', methods=['GET'])
@auth.login_required
@json
def get_auth_token():
    return {'token': g.user.generate_auth_token()}
