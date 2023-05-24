from flask_migrate import Migrate
from infopublic_usuarios.extensions.db import db

migrate = Migrate()

def init_app(app):
    migrate.init_app(app, db)