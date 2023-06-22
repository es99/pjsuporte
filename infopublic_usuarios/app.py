from flask import Flask
from config import config
from infopublic_usuarios.blueprints import main
from infopublic_usuarios.blueprints import auth
from infopublic_usuarios.extensions import db
from infopublic_usuarios.extensions import migrate
from infopublic_usuarios.extensions import bootstrap
from infopublic_usuarios.extensions import login
from infopublic_usuarios.extensions import email
from infopublic_usuarios.extensions import admin


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    main.init_app(app)
    auth.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
    bootstrap.init_app(app)
    login.init_app(app)
    email.init_app(app)
    admin.init_app(app)
    
    return app