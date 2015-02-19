from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail
from flask.ext.restful import Api
from flask.ext.bcrypt import Bcrypt
from config import config

db = SQLAlchemy()
mail = Mail()
bcrypt = Bcrypt()
api_restful = Api()


def create_app(config_name):
    ''' Setup Flask app '''
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    mail.init_app(app)

    # init brcypt  to hass pwasswords
    bcrypt.init_app(app)

    # init api
    api_restful.init_app(app)

    # register blueprints
    from .api_v1 import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    return app
