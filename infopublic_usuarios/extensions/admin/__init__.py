from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from infopublic_usuarios.extensions.db import db, User

admin = Admin()
admin.add_view(ModelView(User, db.session))


def init_app(app):
    admin.init_app(app)
